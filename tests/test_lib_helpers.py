"""Tests for the hand-written (non-generated) surface: the lib/ URL builders,
client.browser, and the client.agent task helpers.

The task helpers must mirror the TypeScript SDK's agentTask/agentBrowserTask:
execute server-side via POST /v1/tools/perform-web-task?sessionId=..., navigate
via the sessions goto API, hold a CDP connection for the task's duration, and
call the endpoint with no HTTP timeout and no retries (a retry would re-run the
task). CDP/WebSocket connections are stubbed; the HTTP layer is respx-mocked.
"""

from __future__ import annotations

import json
from typing import Any

import httpx
import pytest
from respx import MockRouter

import anchorbrowser.resources.tools as tools_module
import anchorbrowser.resources.browser as browser_module
import anchorbrowser.resources.agent_helpers as agent_helpers_module
from anchorbrowser import Anchorbrowser, AsyncAnchorbrowser
from anchorbrowser.lib.browser import BrowserSetup, get_cdp_url, get_agent_ws_url
from anchorbrowser.resources.agent_helpers import _task_kwargs

base_url = "http://127.0.0.1:4010"

SESSION_ID = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
TASK_JSON = {"data": {"result": {"title": "Example Domain"}}}


# ---------------------------------------------------------------------------
# lib/browser.py URL builders
# ---------------------------------------------------------------------------


def test_get_cdp_url() -> None:
    assert (
        get_cdp_url("https://api.anchorbrowser.io", "sid", "key")
        == "wss://connect.anchorbrowser.io?apiKey=key&sessionId=sid"
    )
    assert (
        get_cdp_url("https://api.staging.anchorbrowser.io/", "sid", "key")
        == "wss://connect.staging.anchorbrowser.io?apiKey=key&sessionId=sid"
    )
    # http (local dev) becomes ws, like the TypeScript SDK
    assert get_cdp_url("http://localhost:8080", "sid", "key") == "ws://localhost:8080?apiKey=key&sessionId=sid"


def test_get_agent_ws_url() -> None:
    assert get_agent_ws_url("https://api.anchorbrowser.io", "sid") == "wss://api.anchorbrowser.io/ws?sessionId=sid"
    assert get_agent_ws_url("http://localhost:8080/", "sid") == "ws://localhost:8080/ws?sessionId=sid"


# ---------------------------------------------------------------------------
# _task_kwargs — task_options -> perform_web_task arguments
# ---------------------------------------------------------------------------


def test_task_kwargs_rejects_empty_prompt() -> None:
    with pytest.raises(ValueError, match="Prompt cannot be empty"):
        _task_kwargs("", None)
    with pytest.raises(ValueError, match="Prompt cannot be empty"):
        _task_kwargs("   ", None)


def test_task_kwargs_maps_options() -> None:
    kwargs = _task_kwargs(
        "p",
        {
            "output_schema": {"type": "object"},
            "agent": "browser-use",
            "model": "gpt-5",
            "provider": "openai",
            "max_steps": 7,
            "highlight_elements": True,
            "detect_elements": False,
            "human_intervention": False,
            "secret_values": {"K": "v"},
            # spec-absent fields travel via extra_body
            "extended_system_message": "focus",
            "directly_open_url": True,
            # handled by the helper itself, must not be forwarded
            "url": "https://example.com",
            "on_agent_step": lambda _step: None,
        },
    )
    assert kwargs == {
        "output_schema": {"type": "object"},
        "agent": "browser-use",
        "model": "gpt-5",
        "provider": "openai",
        "max_steps": 7,
        "highlight_elements": True,
        "detect_elements": False,
        "human_intervention": False,
        "secret_values": {"K": "v"},
        "extra_body": {"extended_system_message": "focus", "directly_open_url": True},
    }


def test_task_kwargs_empty_options() -> None:
    assert _task_kwargs("p", None) == {}
    assert _task_kwargs("p", {}) == {}


# ---------------------------------------------------------------------------
# CDP / WebSocket stubs
# ---------------------------------------------------------------------------


@pytest.fixture
def cdp_connections(monkeypatch: pytest.MonkeyPatch) -> list[str]:
    """Stub BrowserSetup's CDP connect/close; records session ids it was entered with."""
    entered: list[str] = []

    def _enter(self: BrowserSetup) -> BrowserSetup:
        entered.append(self.session_id)
        return self

    async def _aenter(self: BrowserSetup) -> BrowserSetup:
        entered.append(self.session_id)
        return self

    def _exit(_self: BrowserSetup, *_args: Any) -> None:
        return None

    async def _aexit(_self: BrowserSetup, *_args: Any) -> None:
        return None

    monkeypatch.setattr(BrowserSetup, "__enter__", _enter)
    monkeypatch.setattr(BrowserSetup, "__exit__", _exit)
    monkeypatch.setattr(BrowserSetup, "__aenter__", _aenter)
    monkeypatch.setattr(BrowserSetup, "__aexit__", _aexit)
    return entered


@pytest.fixture
def agent_step_listeners(monkeypatch: pytest.MonkeyPatch) -> list[tuple[Any, str]]:
    """Stub the WebSocket step listeners; records (callback, session_id)."""
    seen: list[tuple[Any, str]] = []

    def _sync(cb: Any, setup: BrowserSetup) -> None:
        seen.append((cb, setup.session_id))

    def _async(cb: Any, setup: BrowserSetup) -> None:
        seen.append((cb, setup.session_id))

    monkeypatch.setattr(agent_helpers_module, "on_agent_step_sync", _sync)
    monkeypatch.setattr(agent_helpers_module, "on_agent_step_async", _async)
    return seen


# ---------------------------------------------------------------------------
# client.agent.task — sync
# ---------------------------------------------------------------------------


@pytest.mark.respx(base_url=base_url)
def test_task_creates_session_and_performs_web_task(
    client: Anchorbrowser, respx_mock: MockRouter, cdp_connections: list[str]
) -> None:
    respx_mock.post("/v1/sessions").mock(return_value=httpx.Response(200, json={"data": {"id": SESSION_ID}}))
    task_route = respx_mock.post("/v1/tools/perform-web-task").mock(
        return_value=httpx.Response(200, json=TASK_JSON)
    )

    result = client.agent.task("get the title")

    assert result.data is not None and result.data.result == {"title": "Example Domain"}  # type: ignore[union-attr]
    request = task_route.calls.last.request
    assert request.url.params["sessionId"] == SESSION_ID
    assert json.loads(request.content) == {"prompt": "get the title"}
    # a CDP connection was held for the task
    assert cdp_connections == [SESSION_ID]


@pytest.mark.respx(base_url=base_url)
@pytest.mark.usefixtures("cdp_connections")
def test_task_options_reach_the_wire(
    client: Anchorbrowser,
    respx_mock: MockRouter,
    agent_step_listeners: list[tuple[Any, str]],
) -> None:
    respx_mock.post("/v1/sessions").mock(return_value=httpx.Response(200, json={"data": {"id": SESSION_ID}}))
    goto_route = respx_mock.post(f"/v1/sessions/{SESSION_ID}/goto").mock(
        return_value=httpx.Response(200, json={"status": "success"})
    )
    task_route = respx_mock.post("/v1/tools/perform-web-task").mock(
        return_value=httpx.Response(200, json=TASK_JSON)
    )

    def on_step(step: str) -> None:  # pragma: no cover - never invoked here
        pass

    client.agent.task(
        "get the title",
        task_options={
            "url": "https://example.com",
            "on_agent_step": on_step,
            "agent": "browser-use",
            "max_steps": 5,
            "extended_system_message": "focus",
        },
    )

    # url goes through the goto API (like TS), never into the task body
    assert json.loads(goto_route.calls.last.request.content) == {"url": "https://example.com"}
    body = json.loads(task_route.calls.last.request.content)
    assert body == {
        "prompt": "get the title",
        "agent": "browser-use",
        "max_steps": 5,
        "extended_system_message": "focus",  # extra_body merges into the JSON body
    }
    assert agent_step_listeners == [(on_step, SESSION_ID)]


@pytest.mark.respx(base_url=base_url)
@pytest.mark.usefixtures("cdp_connections")
def test_task_reuses_existing_session(client: Anchorbrowser, respx_mock: MockRouter) -> None:
    # no POST /v1/sessions route is registered: creating a session would fail the test
    get_route = respx_mock.get(f"/v1/sessions/{SESSION_ID}").mock(
        return_value=httpx.Response(200, json={"data": {"session_id": SESSION_ID}})
    )
    task_route = respx_mock.post("/v1/tools/perform-web-task").mock(
        return_value=httpx.Response(200, json=TASK_JSON)
    )

    client.agent.task("get the title", session_id=SESSION_ID)

    assert get_route.called
    assert task_route.calls.last.request.url.params["sessionId"] == SESSION_ID


def test_task_rejects_session_id_with_session_options(client: Anchorbrowser) -> None:
    with pytest.raises(ValueError, match="cannot be provided together"):
        client.agent.task("p", session_id=SESSION_ID, session_options={"recording": {"active": False}})


@pytest.mark.respx(base_url=base_url)
@pytest.mark.usefixtures("cdp_connections")
def test_task_fails_when_session_has_no_id(client: Anchorbrowser, respx_mock: MockRouter) -> None:
    respx_mock.post("/v1/sessions").mock(return_value=httpx.Response(200, json={"data": {}}))
    with pytest.raises(ValueError, match="No session ID returned"):
        client.agent.task("get the title")


@pytest.mark.respx(base_url=base_url)
@pytest.mark.usefixtures("cdp_connections")
def test_task_disables_timeout_and_retries(
    client: Anchorbrowser,
    respx_mock: MockRouter,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    respx_mock.post("/v1/sessions").mock(return_value=httpx.Response(200, json={"data": {"id": SESSION_ID}}))
    respx_mock.post("/v1/tools/perform-web-task").mock(return_value=httpx.Response(200, json=TASK_JSON))

    seen: dict[str, Any] = {}
    original = tools_module.ToolsResource.perform_web_task

    def spy(self: Any, **kw: Any) -> Any:
        seen["timeout"] = kw.get("timeout", "NOT PASSED")
        seen["max_retries"] = self._client.max_retries
        return original(self, **kw)

    monkeypatch.setattr(tools_module.ToolsResource, "perform_web_task", spy)

    client.agent.task("get the title")

    assert seen["timeout"] is None, "agent tasks must not inherit the 60s default HTTP timeout"
    assert seen["max_retries"] == 0, "agent tasks must not be retried (a retry re-runs the task)"


# ---------------------------------------------------------------------------
# client.agent.browser_task — sync
# ---------------------------------------------------------------------------


@pytest.mark.respx(base_url=base_url)
def test_browser_task_returns_control_immediately(
    client: Anchorbrowser, respx_mock: MockRouter, cdp_connections: list[str]
) -> None:
    respx_mock.post("/v1/sessions").mock(return_value=httpx.Response(200, json={"data": {"id": SESSION_ID}}))
    respx_mock.post("/v1/tools/perform-web-task").mock(return_value=httpx.Response(200, json=TASK_JSON))

    browser_task = client.agent.browser_task("get the title")

    assert browser_task["session_id"] == SESSION_ID
    # the caller owns the Playwright connection: an unentered context manager
    assert hasattr(browser_task["playwright_browser"], "__enter__")
    assert cdp_connections == []
    # the task runs in the background; the Future resolves to the API response
    result = browser_task["task_result_task"].result(timeout=10)
    assert result.data is not None and result.data.result == {"title": "Example Domain"}


# ---------------------------------------------------------------------------
# client.agent.task / browser_task — async
# ---------------------------------------------------------------------------


@pytest.mark.respx(base_url=base_url)
async def test_async_task(
    async_client: AsyncAnchorbrowser, respx_mock: MockRouter, cdp_connections: list[str]
) -> None:
    respx_mock.post("/v1/sessions").mock(return_value=httpx.Response(200, json={"data": {"id": SESSION_ID}}))
    task_route = respx_mock.post("/v1/tools/perform-web-task").mock(
        return_value=httpx.Response(200, json=TASK_JSON)
    )

    result = await async_client.agent.task("get the title")

    assert result.data is not None and result.data.result == {"title": "Example Domain"}  # type: ignore[union-attr]
    assert task_route.calls.last.request.url.params["sessionId"] == SESSION_ID
    assert cdp_connections == [SESSION_ID]


@pytest.mark.respx(base_url=base_url)
@pytest.mark.usefixtures("cdp_connections")
async def test_async_browser_task(async_client: AsyncAnchorbrowser, respx_mock: MockRouter) -> None:
    respx_mock.post("/v1/sessions").mock(return_value=httpx.Response(200, json={"data": {"id": SESSION_ID}}))
    respx_mock.post("/v1/tools/perform-web-task").mock(return_value=httpx.Response(200, json=TASK_JSON))

    browser_task = await async_client.agent.browser_task("get the title")

    assert browser_task["session_id"] == SESSION_ID
    assert hasattr(browser_task["playwright_browser"], "__aenter__")
    result = await browser_task["task_result_task"]
    assert result.data is not None and result.data.result == {"title": "Example Domain"}


# ---------------------------------------------------------------------------
# client.browser — Playwright connection helpers
# ---------------------------------------------------------------------------


class _DummyContextManager:
    def __enter__(self) -> Any:
        return object()

    def __exit__(self, *args: Any) -> None:
        return None


@pytest.mark.respx(base_url=base_url)
def test_browser_create_connects_to_new_session(
    client: Anchorbrowser, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    respx_mock.post("/v1/sessions").mock(return_value=httpx.Response(200, json={"data": {"id": SESSION_ID}}))

    seen: dict[str, str] = {}

    def fake_connect(api_base_url: str, session_id: str, api_key: str) -> Any:
        seen.update(base_url=api_base_url, session_id=session_id, api_key=api_key)
        return _DummyContextManager()

    monkeypatch.setattr(browser_module, "get_playwright_chromium_from_cdp_url", fake_connect)

    context_manager = client.browser.create()

    assert isinstance(context_manager, _DummyContextManager)
    assert seen["session_id"] == SESSION_ID
    assert seen["api_key"] == client.api_key
    assert seen["base_url"] == str(client.base_url)


def test_browser_connect_uses_given_session(client: Anchorbrowser, monkeypatch: pytest.MonkeyPatch) -> None:
    seen: dict[str, str] = {}

    def fake_connect(_api_base_url: str, session_id: str, _api_key: str) -> Any:
        seen.update(session_id=session_id)
        return _DummyContextManager()

    monkeypatch.setattr(browser_module, "get_playwright_chromium_from_cdp_url", fake_connect)

    client.browser.connect(SESSION_ID)

    assert seen["session_id"] == SESSION_ID
