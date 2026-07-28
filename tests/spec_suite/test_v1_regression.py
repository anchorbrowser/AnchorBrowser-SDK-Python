# yaml-driven spec/manifest handling is inherently untyped
# pyright: reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
"""v1 -> v2 operation regression guard (port of the TS SDK's v1-regression.test.ts).

The coverage suite only cross-checks the CURRENT spec/manifest/client against
each other — it cannot detect an operation the v1 (Stainless) SDK exposed
silently disappearing from the spec during a future sync. This suite checks
every operation of the frozen v1 baseline (extracted from api.md at the
`stainless-baseline` git tag; identical to the TypeScript SDK's baseline)
against the current spec, honoring the manifest's `v1_removed` list of
deliberate, reviewed removals.
"""

from __future__ import annotations

import re

from ._synth import SPEC, MANIFEST, HTTP_METHODS

# Frozen: every operation the v1 (Stainless-generated) SDK exposed.
# NEVER regenerate this list from the current spec — that defeats its purpose.
V1_BASELINE_OPERATIONS = [
    "delete /v1/applications/{application_id}",
    "delete /v1/applications/{application_id}/auth-flows/{auth_flow_id}",
    "delete /v1/identities/{identity_id}",
    "delete /v1/profiles/{name}",
    "delete /v1/sessions/all",
    "delete /v1/sessions/{session_id}",
    "get /v1/applications",
    "get /v1/applications/{application_id}",
    "get /v1/applications/{application_id}/auth-flows",
    "get /v1/applications/{application_id}/identities",
    "get /v1/extensions",
    "get /v1/identities/{identity_id}",
    "get /v1/identities/{identity_id}/credentials",
    "get /v1/profiles",
    "get /v1/profiles/{name}",
    "get /v1/sessions/all/status",
    "get /v1/sessions/{sessionId}/clipboard",
    "get /v1/sessions/{sessionId}/screenshot",
    "get /v1/sessions/{session_id}",
    "get /v1/sessions/{session_id}/downloads",
    "get /v1/sessions/{session_id}/recordings",
    "get /v1/sessions/{session_id}/recordings/primary/fetch",
    "get /v1/tools/perform-web-task/{workflowId}/status",
    "get /v2/tasks/runs/{runId}/status",
    "get /v2/tasks/{taskId}/generation-status",
    "post /v1/applications",
    "post /v1/applications/{application_id}/auth-flows",
    "post /v1/applications/{application_id}/tokens",
    "post /v1/events/{event_name}",
    "post /v1/events/{event_name}/wait",
    "post /v1/identities",
    "post /v1/profiles",
    "post /v1/sessions",
    "post /v1/sessions/{sessionId}/agent/files",
    "post /v1/sessions/{sessionId}/clipboard",
    "post /v1/sessions/{sessionId}/drag-and-drop",
    "post /v1/sessions/{sessionId}/goto",
    "post /v1/sessions/{sessionId}/keyboard/shortcut",
    "post /v1/sessions/{sessionId}/keyboard/type",
    "post /v1/sessions/{sessionId}/mouse/click",
    "post /v1/sessions/{sessionId}/mouse/doubleClick",
    "post /v1/sessions/{sessionId}/mouse/move",
    "post /v1/sessions/{sessionId}/scroll",
    "post /v1/sessions/{sessionId}/uploads",
    "post /v1/tools/fetch-webpage",
    "post /v1/tools/perform-web-task",
    "post /v1/tools/screenshot",
    "post /v2/tasks/generate",
    "post /v2/tasks/{taskId}/run",
    "put /v1/identities/{identity_id}",
]


def _norm(op: str) -> str:
    return re.sub(r"\{[^}]+\}", "{}", op.strip().lower())


current_ops = {
    _norm(f"{m} {p}")
    for p, item in (SPEC.get("paths") or {}).items()
    for m in item
    if m in HTTP_METHODS
}

v1_removed = MANIFEST.get("v1_removed") or []
removed_paths = {_norm(e["path"] if isinstance(e, dict) else e) for e in v1_removed}


def test_every_v1_operation_exists_or_is_declared_removed() -> None:
    gone = [
        op for op in V1_BASELINE_OPERATIONS if _norm(op) not in current_ops and _norm(op) not in removed_paths
    ]
    assert not gone, (
        f"{len(gone)} operation(s) the v1 SDK exposed are missing from spec/openapi.yaml and are NOT "
        "declared in sdk-manifest.yaml's 'v1_removed' list:\n"
        + "\n".join(f"  - {op}" for op in gone)
        + "\nEither restore the operation in the spec (verify against the real backend first) or add it "
        "to 'v1_removed' with a reason if this is a deliberate, reviewed removal."
    )


def test_v1_removed_entries_name_real_baseline_operations() -> None:
    baseline = {_norm(op) for op in V1_BASELINE_OPERATIONS}
    stale = [e for e in removed_paths if e not in baseline]
    assert not stale, f"v1_removed entries that are not v1 baseline operations: {stale}"


def test_v1_removed_entries_have_reasons() -> None:
    missing = [e for e in v1_removed if not isinstance(e, dict) or not e.get("reason")]
    assert not missing, f"v1_removed entries without a reason: {missing}"