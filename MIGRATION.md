# Migrating from v0.x.x to v1

Version 1 regenerates the SDK directly from the public OpenAPI spec instead of
a Stainless build. Client construction, request/response behavior (retries,
timeouts, errors, pydantic response models) and the instance-client calling
style are unchanged — but method names now follow the spec's operation naming
(shared with the [TypeScript SDK](https://github.com/anchorbrowser/AnchorBrowser-SDK-Typescript)),
and a few subsurfaces moved. This guide covers every breaking change; nothing
else changed silently.

## Requirements

Two install requirements changed — `pip` enforces both at install/resolve time:

| Requirement | v0 | v1 |
| --- | --- | --- |
| Python | `>= 3.9` | `>= 3.10` (3.9 is end-of-life) |
| pydantic | `>= 1.9.0, < 3` (v1 supported via a compatibility mode) | `>= 2, < 3` — **pydantic v1 is no longer supported** |

If your project pins pydantic v1, upgrade it before upgrading the SDK — `pip` will refuse
to resolve `anchorbrowser >= 1.0.0` alongside `pydantic < 2`.

Every other runtime dependency keeps the same version range as v0 (`httpx`,
`typing-extensions`, `anyio`, `distro`, `sniffio`, `websockets`, `playwright`, and the
optional `aiohttp` extra).

## Client construction — unchanged

```python
from anchorbrowser import Anchorbrowser  # or AsyncAnchorbrowser

client = Anchorbrowser()  # reads ANCHORBROWSER_API_KEY from the environment
```

`max_retries`, `timeout`, `base_url`, `http_client`, `with_options(...)` and
the exception hierarchy (`APIStatusError`, `RateLimitError`, …) all work
exactly as before.

## Method renames

Every method keeps the `client.<resource>.<method>(...)` shape and its
argument style (positional path params, keyword query/body params). Nested
sub-resources (`client.sessions.mouse.click`) are now flat methods
(`client.sessions.mouse_click`). The full mapping:

| Endpoint | v0 | v1 |
| --- | --- | --- |
| `delete /v1/applications/{application_id}` | `client.applications.delete(...)` | `client.applications.delete_application(...)` |
| `delete /v1/applications/{application_id}/auth-flows/{auth_flow_id}` | `client.applications.auth_flows.delete(...)` | `client.applications.delete_auth_flow(...)` |
| `delete /v1/identities/{identity_id}` | `client.identities.delete(...)` | `client.identities.delete_identity(...)` |
| `delete /v1/profiles/{name}` | `client.profiles.delete(...)` | `client.profiles.delete_profile(...)` |
| `delete /v1/sessions/all` | `client.sessions.all.delete(...)` | `client.sessions.delete_all_sessions(...)` |
| `delete /v1/sessions/{session_id}` | `client.sessions.delete(...)` | `client.sessions.delete_session(...)` |
| `get /v1/applications` | `client.applications.list(...)` | `client.applications.list_applications(...)` |
| `get /v1/applications/{application_id}` | `client.applications.retrieve(...)` | `client.applications.get_application(...)` |
| `get /v1/applications/{application_id}/auth-flows` | `client.applications.auth_flows.list(...)` | `client.applications.list_auth_flows(...)` |
| `get /v1/applications/{application_id}/identities` | `client.applications.list_identities(...)` | `client.applications.list_application_identities(...)` |
| `get /v1/extensions` | `client.extensions.list(...)` | `client.extensions.list_extensions(...)` |
| `get /v1/identities/{identity_id}` | `client.identities.retrieve(...)` | `client.identities.get_identity(...)` |
| `get /v1/profiles` | `client.profiles.list(...)` | `client.profiles.list_profiles(...)` |
| `get /v1/profiles/{name}` | `client.profiles.retrieve(...)` | `client.profiles.get_profile(...)` |
| `get /v1/sessions/all/status` | `client.sessions.all.status(...)` | `client.sessions.get_all_sessions_status(...)` |
| `get /v1/sessions/{sessionId}/clipboard` | `client.sessions.clipboard.get(...)` | `client.sessions.get_clipboard(...)` |
| `get /v1/sessions/{sessionId}/screenshot` | `client.sessions.retrieve_screenshot(...)` | `client.sessions.get_session_screenshot(...)` |
| `get /v1/sessions/{session_id}` | `client.sessions.retrieve(...)` | `client.sessions.get_session(...)` |
| `get /v1/sessions/{session_id}/downloads` | `client.sessions.retrieve_downloads(...)` | `client.sessions.get_session_downloads(...)` |
| `get /v1/sessions/{session_id}/recordings` | `client.sessions.recordings.list(...)` | `client.recordings.list_recordings(...)` |
| `get /v1/sessions/{session_id}/recordings/primary/fetch` | `client.sessions.recordings.primary.get(...)` | `client.recordings.fetch_primary_recording(...)` |
| `get /v1/tools/perform-web-task/{workflowId}/status` | `client.tools.get_perform_web_task_status(...)` | `client.tools.get_perform_web_task_status(...)` (unchanged) |
| `get /v2/tasks/runs/{runId}/status` | `client.tasks.runs.get_status(...)` | `client.tasks.get_task_run_status(...)` |
| `get /v2/tasks/{taskId}/generation-status` | `client.tasks.generations.get_status(...)` | `client.tasks.get_task_generation_status(...)` |
| `post /v1/applications` | `client.applications.create(...)` | `client.applications.create_application(...)` |
| `post /v1/applications/{application_id}/auth-flows` | `client.applications.auth_flows.create(...)` | `client.applications.create_auth_flow(...)` |
| `post /v1/applications/{application_id}/tokens` | `client.applications.create_identity_token(...)` | `client.applications.create_identity_token(...)` (unchanged) |
| `post /v1/events/{event_name}` | `client.events.signal(...)` | `client.events.signal_event(...)` |
| `post /v1/events/{event_name}/wait` | `client.events.wait_for(...)` | `client.events.wait_for_event(...)` |
| `post /v1/identities` | `client.identities.create(...)` | `client.identities.create_identity(...)` |
| `post /v1/profiles` | `client.profiles.create(...)` | `client.profiles.create_profile(...)` |
| `post /v1/sessions` | `client.sessions.create(...)` | `client.sessions.create_session(...)` |
| `post /v1/sessions/{sessionId}/agent/files` | `client.sessions.agent.files.upload(...)` | `client.agent.upload_agent_files(...)` |
| `post /v1/sessions/{sessionId}/clipboard` | `client.sessions.clipboard.set(...)` | `client.sessions.set_clipboard(...)` |
| `post /v1/sessions/{sessionId}/keyboard/shortcut` | `client.sessions.keyboard.shortcut(...)` | `client.sessions.keyboard_shortcut(...)` |
| `post /v1/sessions/{sessionId}/keyboard/type` | `client.sessions.keyboard.type(...)` | `client.sessions.keyboard_type(...)` |
| `post /v1/sessions/{sessionId}/mouse/click` | `client.sessions.mouse.click(...)` | `client.sessions.mouse_click(...)` |
| `post /v1/sessions/{sessionId}/mouse/doubleClick` | `client.sessions.mouse.double_click(...)` | `client.sessions.mouse_double_click(...)` |
| `post /v1/sessions/{sessionId}/mouse/move` | `client.sessions.mouse.move(...)` | `client.sessions.mouse_move(...)` |
| `post /v2/tasks/generate` | `client.tasks.generate(...)` | `client.tasks.generate_task(...)` |
| `post /v2/tasks/{taskId}/run` | `client.tasks.run(...)` | `client.tasks.run_task(...)` |
| `put /v1/identities/{identity_id}` | `client.identities.update(...)` | `client.identities.update_identity(...)` |

Methods not listed kept their names (`client.sessions.goto`,
`client.sessions.scroll`, `client.sessions.drag_and_drop`,
`client.sessions.upload_file`, `client.tools.perform_web_task`,
`client.tools.screenshot_webpage`, …). The v1 surface also exposes many
endpoints the v0 SDK never had (webhooks, batch sessions, certificates,
integrations, billing, session pages/status/recording control) — see the
[SDK reference](https://docs.anchorbrowser.io/sdk-reference/overview).

Two examples:

```diff
- session = client.sessions.create(session={"recording": {"active": False}})
+ session = client.sessions.create_session(session={"recording": {"active": False}})

- client.sessions.mouse.click(session_id, x=100, y=200)
+ client.sessions.mouse_click(session_id, x=100, y=200)
```

## Removed endpoints

- `client.tools.fetch_webpage(...)` **still exists but calls a different
  endpoint**: the deprecated `POST /v1/tools/fetch-webpage` was replaced by the
  Web Unlocker endpoint `POST /v1/tools/fetch/webpage` (different parameters —
  see the SDK reference).
- `client.identities.retrieve_credentials(...)` was removed: it returned raw
  stored secrets and is not part of the public API.

## `with_raw_response` / `with_streaming_response` removed

The per-method wrapper layer is gone. To inspect raw response data (headers,
status) use the generic verbs, which respect client options like retries:

```diff
- response = client.sessions.with_raw_response.create()
- print(response.headers)
- session = response.parse()
+ import httpx
+ response = client.post("/v1/sessions", cast_to=httpx.Response, body={})
+ print(response.headers)
+ session = response.json()
```

Binary endpoints (screenshots, recordings, PDFs) return a `BinaryAPIResponse`
with `.read()` / `.write_to_file(...)` — same as before.

## Types module

- Response models: `anchorbrowser.types.models` (one model per named schema
  and per operation response).
- Request TypedDicts: `anchorbrowser.types.params`.

The old per-operation modules (`anchorbrowser.types.session_create_params`,
etc.) no longer exist. Response **shapes are unchanged** — field names and
nesting still match the API exactly (e.g. `session.data.id` after
`create_session`).

## Small fixes you may notice

- `client.browser` and `client.agent` were broken in v0
  (`AttributeError` — the properties were declared but never wired up). They
  now work: `client.agent.task("...")`, `client.browser.create()`,
  `client.browser.connect(session_id)`.
- `client.agent.task(...)` now executes server-side via the perform-web-task
  API (`POST /v1/tools/perform-web-task`), exactly like the TypeScript SDK's
  `agentTask` — the old in-browser extension mechanism is gone. It returns the
  perform-web-task response model (the agent's output is `result.data.result`)
  instead of a string, and the call is made with no HTTP timeout and no
  retries (a retry would re-run the task).
- `client.agent.browser_task(...)` now actually returns control immediately:
  `task_result_task` is a `concurrent.futures.Future` (sync client) or an
  `asyncio.Task` (async client) — call `.result()` / `await` it for the task
  result.
- `client.sessions.mouse_click(...)`'s optional click `timeout` body parameter
  is the keyword `timeout_` (the plain `timeout` keyword remains the
  per-request HTTP timeout, as on every method).
- 28 operations that previously returned untyped data now return pydantic
  models with full autocomplete (e.g. `get_session`, `mouse_click`,
  `list_batch_sessions`).
