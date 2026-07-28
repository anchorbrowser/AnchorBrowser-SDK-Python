"""Wire-parity suite (Python port of the TS SDK's tests/parity/wire.test.ts).

Every operation in spec/openapi.yaml + spec/sdk-manifest.yaml is invoked
through its SDK method with deterministic synthesized arguments against a
local capture server, and the exact request (method, path, query, auth /
content headers, body) is compared to the committed golden file.

The async client is exercised over the same operations and must produce
requests identical to the sync client's.

After an INTENTIONAL wire change, regenerate the golden:
    ./scripts/update-wire-golden
and review the diff — it is the reviewable record of the change.
"""

from __future__ import annotations

import json
from typing import Any
from pathlib import Path

import anyio
import pytest

from anchorbrowser import Anchorbrowser, AsyncAnchorbrowser

from ._synth import all_operations
from ._capture import CaptureServer, invoke, normalize

GOLDEN_PATH = Path(__file__).parent / "wire_parity_golden.json"

OPS = all_operations()


@pytest.fixture(scope="module")
def server() -> Any:
    s = CaptureServer()
    yield s
    s.stop()


@pytest.fixture(scope="module")
def golden() -> dict[str, Any]:
    assert GOLDEN_PATH.exists(), "wire_parity_golden.json missing — run ./scripts/update-wire-golden"
    return json.loads(GOLDEN_PATH.read_text())


def test_operation_count(golden: dict[str, Any]) -> None:
    assert len(OPS) == len({op.name for op in OPS})
    assert golden["__operation_count__"] == len(OPS)


@pytest.mark.parametrize("op", OPS, ids=lambda o: o.name)
def test_wire_parity_sync(op: Any, server: Any, golden: dict[str, Any]) -> None:
    client = Anchorbrowser(api_key="test-api-key", base_url=server.base_url, max_retries=0)
    before = len(server.captured)
    invoke(client, op)
    assert len(server.captured) == before + 1
    raw = server.captured[-1]

    # every request must be identifiable in access logs / Datadog
    assert raw["headers"].get("user-agent", "").startswith("Anchorbrowser/Python")
    assert raw["headers"].get("x-anchor-sdk", "").startswith("python/")

    got = normalize(raw)
    assert op.name in golden, f"missing golden entry for {op.name} — run ./scripts/update-wire-golden"
    assert got == golden[op.name]


@pytest.mark.parametrize("op", OPS, ids=lambda o: o.name)
def test_wire_parity_async_matches_sync(op: Any, server: Any) -> None:
    sync_client = Anchorbrowser(api_key="test-api-key", base_url=server.base_url, max_retries=0)
    before = len(server.captured)
    invoke(sync_client, op)
    sync_req = normalize(server.captured[-1])

    async def run_async() -> None:
        client = AsyncAnchorbrowser(api_key="test-api-key", base_url=server.base_url, max_retries=0)
        resource = getattr(client, op.py_attr)
        method = getattr(resource, op.py_method)
        args, kwargs = op.build_kwargs()
        await method(*args, **kwargs)
        await client.close()

    anyio.run(run_async)
    async_req = normalize(server.captured[-1])
    assert len(server.captured) == before + 2

    for key in ("method", "path", "query", "body", "headers"):
        assert async_req[key] == sync_req[key], f"async {key} differs from sync"
