# yaml-driven spec/manifest handling is inherently untyped
# pyright: reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
"""Spec-coverage suite (Python port of the TS SDK's tests/spec/coverage.test.ts).

Keeps spec/openapi.yaml, spec/sdk-manifest.yaml, and the generated client
surface in lockstep:
  - every spec operation has a manifest naming entry (no auto-derived names)
  - every manifest naming entry points at a real spec operation
  - every mapped operation is a real, callable method on BOTH clients
  - no generated resource method exists without a spec operation behind it
"""

from __future__ import annotations

import inspect
from typing import Any

from anchorbrowser import Anchorbrowser, AsyncAnchorbrowser

from ._synth import SPEC, MANIFEST, HTTP_METHODS, snake

NAMING: dict[str, Any] = MANIFEST.get("naming", {})

spec_ops = {
    f"{m} {p}"
    for p, item in (SPEC.get("paths") or {}).items()
    for m in item
    if m in HTTP_METHODS
}


def test_every_spec_operation_has_a_naming_entry() -> None:
    unnamed = sorted(op for op in spec_ops if op not in NAMING)
    assert not unnamed, (
        "Operations without an sdk-manifest.yaml naming entry (would get auto-derived names):\n"
        + "\n".join(f"  - {op}" for op in unnamed)
    )


def test_every_naming_entry_points_at_a_real_operation() -> None:
    stale = sorted(op for op in NAMING if op not in spec_ops)
    assert not stale, (
        "sdk-manifest.yaml naming entries with no matching operation in openapi.yaml:\n"
        + "\n".join(f"  - {op}" for op in stale)
    )


def _assert_methods_exist(client: Any) -> None:
    missing: list[str] = []
    for key, entry in NAMING.items():
        attr = snake(entry["class"])
        method = snake(entry["method"])
        resource = getattr(client, attr, None)
        if resource is None or not callable(getattr(resource, method, None)):
            missing.append(f"{key} -> client.{attr}.{method}")
    assert not missing, (
        "Manifest methods with no matching client method — run ./scripts/generate:\n"
        + "\n".join(f"  - {m}" for m in missing)
    )


def test_sync_client_exposes_every_mapped_method() -> None:
    _assert_methods_exist(Anchorbrowser(api_key="k"))


def test_async_client_exposes_every_mapped_method() -> None:
    _assert_methods_exist(AsyncAnchorbrowser(api_key="k"))


def test_no_orphan_generated_methods() -> None:
    """Every public method on a generated resource maps back to a spec operation."""
    expected: dict[str, set[str]] = {}
    for entry in NAMING.values():
        expected.setdefault(snake(entry["class"]), set()).add(snake(entry["method"]))

    client = Anchorbrowser(api_key="k")
    orphans: list[str] = []
    for attr, methods in expected.items():
        resource = getattr(client, attr)
        public = {
            name
            for name, _member in inspect.getmembers(type(resource), predicate=inspect.isfunction)
            if not name.startswith("_")
        }
        # hand-written helpers are allowed only on the agent resource
        if attr == "agent":
            public -= {"task", "browser_task"}
        for name in sorted(public - methods):
            orphans.append(f"client.{attr}.{name}")
    assert not orphans, "Generated methods with no spec operation behind them:\n" + "\n".join(
        f"  - {o}" for o in orphans
    )