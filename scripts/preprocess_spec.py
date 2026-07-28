#!/usr/bin/env python3
# yaml-driven spec/manifest handling is inherently untyped
# pyright: reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
"""Preprocess spec/openapi.yaml for code generation.

Operations whose 2xx JSON response schema is written inline in the spec would
otherwise generate as untyped ``object`` returns. This script hoists each such
schema into ``components.schemas`` under a deterministic name derived from the
sdk-manifest naming entry (class ``Sessions`` + method ``getSession`` ->
``SessionsGetSessionResponse``) and replaces it with a ``$ref``, so both
datamodel-code-generator and scripts/generate_resources.py see a named model —
mirroring the typed per-operation responses of the TypeScript SDK.

Only object-shaped schemas are hoisted; inline arrays/primitives (and
operations without a manifest entry) keep their untyped return and are listed
on stderr. The result is written to --out; spec/openapi.yaml is never modified.
"""

from __future__ import annotations

import re
import sys
import argparse
from typing import Any
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
HTTP_METHODS = {"get", "post", "put", "patch", "delete"}
# must match first_2xx() in scripts/generate_resources.py — only the first
# matching status' response becomes the operation's return type
FIRST_2XX = ("200", "201", "202", "204")


def pascal(name: str) -> str:
    return "".join(part[:1].upper() + part[1:] for part in re.split(r"[_\-\s]+", name) if part)


def hoisted_response_name(class_name: str, method_name: str) -> str:
    return f"{pascal(class_name)}{pascal(method_name)}Response"


def hoistable(schema: Any) -> bool:
    """Only object-shaped schemas become models; arrays/primitives stay untyped."""
    if not isinstance(schema, dict) or "$ref" in schema:
        return False
    if not any(k in schema for k in ("properties", "allOf", "oneOf", "anyOf")):
        return False
    return bool(schema.get("type", "object") == "object")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    spec: dict[str, Any] = yaml.safe_load((REPO / "spec" / "openapi.yaml").read_text())
    manifest: dict[str, Any] = yaml.safe_load((REPO / "spec" / "sdk-manifest.yaml").read_text())
    naming: dict[str, Any] = manifest.get("naming", {})
    schemas: dict[str, Any] = spec.setdefault("components", {}).setdefault("schemas", {})

    hoisted = 0
    for path, path_item in (spec.get("paths") or {}).items():
        for http_method, op in path_item.items():
            if http_method not in HTTP_METHODS:
                continue
            responses = op.get("responses") or {}
            status = next((s for s in FIRST_2XX if s in responses), None)
            if status is None:
                continue
            media = ((responses[status] or {}).get("content") or {}).get("application/json")
            if not media:
                continue
            schema = media.get("schema")
            if schema is None or "$ref" in schema:
                continue
            entry = naming.get(f"{http_method} {path}")
            if not entry or not hoistable(schema):
                print(f"note: {http_method} {path} {status} response stays untyped (inline non-object schema)", file=sys.stderr)
                continue
            name = hoisted_response_name(entry["class"], entry["method"])
            if name in schemas and schemas[name] != schema:
                raise SystemExit(f"error: hoisted response name '{name}' collides with an existing schema")
            schemas[name] = schema
            media["schema"] = {"$ref": f"#/components/schemas/{name}"}
            hoisted += 1

    Path(args.out).write_text(yaml.safe_dump(spec, sort_keys=False, allow_unicode=True))
    print(f"preprocess_spec: hoisted {hoisted} inline response schemas -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
