"""Hand-written AI-agent helpers layered on top of the generated Agent API resource.

`client.agent` exposes both the generated Agent API endpoints (agent files,
pause/resume, human interventions — see resources/agent.py, generated) and
these task helpers. Tasks execute server-side through the perform-web-task
API (`POST /v1/tools/perform-web-task?sessionId=...`), mirroring the
TypeScript SDK's `agentTask` / `agentBrowserTask`. This file is never touched
by scripts/generate.
"""

from __future__ import annotations

import asyncio
from typing import Any, Optional
from concurrent.futures import Future, ThreadPoolExecutor

from .agent import AgentResource, AsyncAgentResource
from ..types import models
from ..lib.agent import on_agent_step_sync, on_agent_step_async
from ..lib.browser import (
    BrowserSetup,
    AgentTaskParams,
    BrowserTaskResponse,
)
from ..types.params import SessionConfig

__all__ = ["AgentHelpersResource", "AsyncAgentHelpersResource"]

# task_options keys forwarded verbatim to tools.perform_web_task
_BODY_KEYS = (
    "output_schema",
    "agent",
    "highlight_elements",
    "model",
    "provider",
    "detect_elements",
    "human_intervention",
    "max_steps",
    "secret_values",
)
# accepted by the backend but not (yet) in the public OpenAPI spec — sent via extra_body
_EXTRA_BODY_KEYS = ("extended_system_message", "directly_open_url")


def _task_kwargs(prompt: str, task_options: Optional[AgentTaskParams]) -> dict[str, Any]:
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    opts: dict[str, Any] = dict(task_options or {})
    kwargs: dict[str, Any] = {k: opts[k] for k in _BODY_KEYS if opts.get(k) is not None}
    extra_body = {k: opts[k] for k in _EXTRA_BODY_KEYS if opts.get(k) is not None}
    if extra_body:
        kwargs["extra_body"] = extra_body
    return kwargs


class AgentHelpersResource(AgentResource):
    def task(
        self,
        prompt: str,
        *,
        session_options: Optional[SessionConfig] = None,
        task_options: Optional[AgentTaskParams] = None,
        session_id: Optional[str] = None,
    ) -> models.PerformWebTaskResponseSchema:
        """Execute an AI agent task within a browser session and wait for the result.

        Creates a new browser session (or reuses `session_id`), optionally navigates
        to `task_options["url"]`, optionally streams agent steps over WebSocket
        (`task_options["on_agent_step"]`), and runs the prompt server-side via the
        perform-web-task API. A live CDP connection is held for the duration of the
        task and closed when it finishes.

        Args:
            prompt (str): The task prompt/instruction for the AI agent to execute.
            session_options (Optional[SessionConfig], optional): Configuration options for the
                browser session. Defaults to None, which creates a session with default settings.
            task_options (Optional[AgentTaskParams], optional): Additional task configuration
            session_id (Optional[str], optional): Reuse an existing session instead of creating one.

        Returns:
            The perform-web-task response; the agent's output is in `.data.result`.
        """
        kwargs = _task_kwargs(prompt, task_options)
        if session_id and session_options:
            raise ValueError("session_id and session_options cannot be provided together")
        if session_id:
            retrieved_session = self._client.sessions.get_session(session_id)
            if not retrieved_session.data or not retrieved_session.data.session_id:
                raise ValueError("Failed to retrieve session: No session ID returned")
            actual_session_id = retrieved_session.data.session_id
        else:
            created_session = self._client.sessions.create_session(session=session_options or {})
            if not created_session or not created_session.data or not created_session.data.id:
                raise ValueError("Failed to create session: No session ID returned")
            actual_session_id = created_session.data.id

        with BrowserSetup(
            session_id=actual_session_id,
            base_url=str(self._client.base_url),
            api_key=self._client.api_key,
        ) as browser_setup:
            if task_options:
                url = task_options.get("url")
                if url:
                    self._client.sessions.goto(actual_session_id, url=url)
                on_agent_step = task_options.get("on_agent_step")
                if on_agent_step:
                    on_agent_step_sync(on_agent_step, browser_setup)
            # agent tasks can run for many minutes: no HTTP timeout, and no retries
            # (a retry would re-run the task) — matching the TypeScript agentTask
            return self._client.with_options(max_retries=0).tools.perform_web_task(
                prompt=prompt,
                session_id=actual_session_id,
                timeout=None,
                **kwargs,
            )

    def browser_task(
        self,
        prompt: str,
        *,
        session_options: Optional[SessionConfig] = None,
        task_options: Optional[AgentTaskParams] = None,
    ) -> BrowserTaskResponse:
        """Start an AI agent task but return control to the caller immediately.

        Creates a new browser session, starts the prompt server-side via the
        perform-web-task API in a background thread, and returns without waiting,
        so the caller can drive the same session with Playwright while the agent
        works.

        Args:
            prompt (str): The task prompt/instruction for the AI agent to execute.
            session_options (Optional[SessionConfig], optional): Configuration options for the
                browser session. Defaults to None, which creates a session with default settings.
            task_options (Optional[AgentTaskParams], optional): Additional task configuration including:
                output_schema, url, on_agent_step. Defaults to None.

        Returns:
            Response dict containing:
                - session_id: The ID of the created browser session
                - task_result_task: a `concurrent.futures.Future` — call `.result()` for the task result
                - playwright_browser: a context manager connecting Playwright to the session (`with ... as browser:`)
        """
        kwargs = _task_kwargs(prompt, task_options)
        session = self._client.sessions.create_session(session=session_options or {})
        if not session.data or not session.data.id:
            raise ValueError("Failed to create session: No session ID returned")
        actual_session_id = session.data.id

        browser_setup = BrowserSetup(
            session_id=actual_session_id,
            base_url=str(self._client.base_url),
            api_key=self._client.api_key,
        )
        if task_options:
            url = task_options.get("url")
            if url:
                self._client.sessions.goto(actual_session_id, url=url)
            on_agent_step = task_options.get("on_agent_step")
            if on_agent_step:
                on_agent_step_sync(on_agent_step, browser_setup)

        # agent tasks can run for many minutes: no HTTP timeout, and no retries
        # (a retry would re-run the task) — matching the TypeScript agentBrowserTask
        run_client = self._client.with_options(max_retries=0)
        executor = ThreadPoolExecutor(max_workers=1)
        task_future: Future[models.PerformWebTaskResponseSchema] = executor.submit(
            lambda: run_client.tools.perform_web_task(
                prompt=prompt,
                session_id=actual_session_id,
                timeout=None,
                **kwargs,
            )
        )
        executor.shutdown(wait=False)

        return BrowserTaskResponse(
            session_id=actual_session_id,
            task_result_task=task_future,
            playwright_browser=browser_setup.browser_generator,
        )


class AsyncAgentHelpersResource(AsyncAgentResource):
    async def task(
        self,
        prompt: str,
        *,
        session_options: Optional[SessionConfig] = None,
        task_options: Optional[AgentTaskParams] = None,
        session_id: Optional[str] = None,
    ) -> models.PerformWebTaskResponseSchema:
        """Execute an AI agent task within a browser session and wait for the result.

        Creates a new browser session (or reuses `session_id`), optionally navigates
        to `task_options["url"]`, optionally streams agent steps over WebSocket
        (`task_options["on_agent_step"]`), and runs the prompt server-side via the
        perform-web-task API. A live CDP connection is held for the duration of the
        task and closed when it finishes.

        Args:
            prompt (str): The task prompt/instruction for the AI agent to execute.
            session_options (Optional[SessionConfig], optional): Configuration options for the
                browser session. Defaults to None, which creates a session with default settings.
            task_options (Optional[AgentTaskParams], optional): Additional task configuration
            session_id (Optional[str], optional): Reuse an existing session instead of creating one.

        Returns:
            The perform-web-task response; the agent's output is in `.data.result`.
        """
        kwargs = _task_kwargs(prompt, task_options)
        if session_id and session_options:
            raise ValueError("session_id and session_options cannot be provided together")
        if session_id:
            retrieved_session = await self._client.sessions.get_session(session_id)
            if not retrieved_session.data or not retrieved_session.data.session_id:
                raise ValueError("Failed to retrieve session: No session ID returned")
            actual_session_id = retrieved_session.data.session_id
        else:
            created_session = await self._client.sessions.create_session(session=session_options or {})
            if not created_session or not created_session.data or not created_session.data.id:
                raise ValueError("Failed to create session: No session ID returned")
            actual_session_id = created_session.data.id

        browser_setup = BrowserSetup(
            session_id=actual_session_id,
            base_url=str(self._client.base_url),
            api_key=self._client.api_key,
        )

        async with browser_setup:
            if task_options:
                url = task_options.get("url")
                if url:
                    await self._client.sessions.goto(actual_session_id, url=url)
                on_agent_step = task_options.get("on_agent_step")
                if on_agent_step:
                    on_agent_step_async(on_agent_step, browser_setup)
            # agent tasks can run for many minutes: no HTTP timeout, and no retries
            # (a retry would re-run the task) — matching the TypeScript agentTask
            return await self._client.with_options(max_retries=0).tools.perform_web_task(
                prompt=prompt,
                session_id=actual_session_id,
                timeout=None,
                **kwargs,
            )

    async def browser_task(
        self,
        prompt: str,
        *,
        session_options: Optional[SessionConfig] = None,
        task_options: Optional[AgentTaskParams] = None,
    ) -> BrowserTaskResponse:
        """Start an AI agent task but return control to the caller immediately.

        Creates a new browser session, starts the prompt server-side via the
        perform-web-task API as an asyncio task, and returns without awaiting it,
        so the caller can drive the same session with Playwright while the agent
        works.

        Args:
            prompt (str): The task prompt/instruction for the AI agent to execute.
            session_options (Optional[SessionConfig], optional): Configuration options for the
                browser session. Defaults to None, which creates a session with default settings.
            task_options (Optional[AgentTaskParams], optional): Additional task configuration including:
                output_schema, url, on_agent_step. Defaults to None.

        Returns:
            Response dict containing:
                - session_id: The ID of the created browser session
                - task_result_task: an `asyncio.Task` — await it for the task result
                - playwright_browser: an async context manager connecting Playwright to the session
        """
        kwargs = _task_kwargs(prompt, task_options)
        session = await self._client.sessions.create_session(session=session_options or {})
        if not session.data or not session.data.id:
            raise ValueError("Failed to create session: No session ID returned")
        actual_session_id = session.data.id

        browser_setup = BrowserSetup(
            session_id=actual_session_id,
            base_url=str(self._client.base_url),
            api_key=self._client.api_key,
        )
        if task_options:
            url = task_options.get("url")
            if url:
                await self._client.sessions.goto(actual_session_id, url=url)
            on_agent_step = task_options.get("on_agent_step")
            if on_agent_step:
                on_agent_step_async(on_agent_step, browser_setup)

        # agent tasks can run for many minutes: no HTTP timeout, and no retries
        # (a retry would re-run the task) — matching the TypeScript agentBrowserTask
        task_result_task: asyncio.Task[models.PerformWebTaskResponseSchema] = asyncio.ensure_future(
            self._client.with_options(max_retries=0).tools.perform_web_task(
                prompt=prompt,
                session_id=actual_session_id,
                timeout=None,
                **kwargs,
            )
        )

        return BrowserTaskResponse(
            session_id=actual_session_id,
            task_result_task=task_result_task,
            playwright_browser=browser_setup.async_browser_generator,
        )
