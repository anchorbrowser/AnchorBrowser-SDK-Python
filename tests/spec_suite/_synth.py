# yaml-driven spec/manifest handling is inherently untyped
# pyright: reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
"""Deterministic request-argument synthesis from the OpenAPI spec.

Python port of the TypeScript SDK's tests/parity/synthesize.ts: for every
operation the wire-parity suite builds a minimal, fixed call — required
path/query parameters and (when required) a request body with only the
required properties. Values are constant so the golden file is stable.
"""

from __future__ import annotations

import re
import keyword
from typing import Any
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent.parent
SPEC = yaml.safe_load((REPO / "spec" / "openapi.yaml").read_text())
MANIFEST = yaml.safe_load((REPO / "spec" / "sdk-manifest.yaml").read_text())

HTTP_METHODS = {"get", "post", "put", "patch", "delete"}
RESERVED_PARAM_NAMES = {"extra_headers", "extra_query", "extra_body", "timeout", "self"}

FIXED = {
    "uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "string": "string",
    "url": "https://example.com",
    "date_time": "2024-01-01T12:00:00Z",
    "int": 1,
    "number": 1,
    "bool": True,
}


def snake(name: str) -> str:
    s = re.sub(r"[-\s]+", "_", name)
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", s)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    s = s.replace("__", "_").lower()
    if keyword.iskeyword(s) or s in RESERVED_PARAM_NAMES:
        s += "_"
    return s


def resolve(schema: dict[str, Any] | None) -> dict[str, Any]:
    if schema and "$ref" in schema:
        name = schema["$ref"].split("/")[-1]
        return SPEC.get("components", {}).get("schemas", {}).get(name, {"type": "object"})
    return schema or {}


def build_value(raw: dict[str, Any] | None, depth: int = 0) -> Any:
    if depth > 6:
        return {}
    schema = resolve(raw)
    if "example" in schema:
        return schema["example"]
    if "default" in schema:
        return schema["default"]
    enum = schema.get("enum")
    if isinstance(enum, list) and enum:
        return enum[0]
    if isinstance(schema.get("allOf"), list):
        merged: dict[str, Any] = {"type": "object", "properties": {}, "required": []}
        for part in schema["allOf"]:
            r = resolve(part)
            merged["properties"].update(r.get("properties") or {})
            merged["required"].extend(r.get("required") or [])
        return build_value(merged, depth + 1)
    for key in ("oneOf", "anyOf"):
        subs = schema.get(key)
        if isinstance(subs, list) and subs:
            return build_value(subs[0], depth + 1)
    t = schema.get("type")
    if t == "string":
        fmt = schema.get("format")
        if fmt == "uuid":
            return FIXED["uuid"]
        if fmt in ("uri", "url"):
            return FIXED["url"]
        if fmt == "date-time":
            return FIXED["date_time"]
        if fmt == "binary":
            return ("example.txt", b"Example data")
        return FIXED["string"]
    if t == "integer":
        return FIXED["int"]
    if t == "number":
        return FIXED["number"]
    if t == "boolean":
        return FIXED["bool"]
    if t == "array":
        return [build_value(schema.get("items"), depth + 1)]
    out: dict[str, Any] = {}
    for name in schema.get("required") or []:
        out[name] = build_value((schema.get("properties") or {}).get(name), depth + 1)
    return out


class Op:
    def __init__(self, path: str, http_method: str, opdef: dict[str, Any], class_name: str, method_name: str) -> None:
        self.path = path
        self.http_method = http_method
        self.opdef = opdef
        self.class_name = class_name
        self.py_attr = snake(class_name)
        self.py_method = snake(method_name)
        self.name = f"{class_name}.{method_name}"

    def build_kwargs(self) -> tuple[list[str], dict[str, Any]]:
        """Returns (positional path args, keyword args) for the SDK method call."""
        args: list[str] = []
        kwargs: dict[str, Any] = {}
        params = [resolve(p) if "$ref" in p else p for p in self.opdef.get("parameters", [])]
        for p in params:
            if p.get("in") == "path":
                name = str(p["name"])
                args.append(
                    str(FIXED["uuid"]) if re.search(r"id$", name, re.I) else f"your-{snake(name).replace('_', '-')}"
                )
            elif p.get("in") == "query" and p.get("required"):
                kwargs[snake(str(p["name"]))] = build_value(p.get("schema") or {"type": "string"}, 1)
        body = self.opdef.get("requestBody")
        if body:
            body = resolve(body) if "$ref" in body else body
            if body.get("required"):
                content = body.get("content") or {}
                ctype = "application/json" if "application/json" in content else next(iter(content), None)
                if ctype:
                    schema = resolve(content[ctype].get("schema"))
                    required = set(schema.get("required") or [])
                    for prop, prop_schema in (schema.get("properties") or {}).items():
                        if prop in required:
                            kwargs[snake(prop)] = build_value(prop_schema, 1)
        return args, kwargs

    def success_content_type(self) -> str:
        for status in ("200", "201", "202", "204"):
            resp = (self.opdef.get("responses") or {}).get(status)
            if resp:
                content = resp.get("content") or {}
                if content:
                    return next(iter(content))
        return "application/json"


def all_operations() -> list[Op]:
    naming = MANIFEST.get("naming", {})
    ops: list[Op] = []
    for path, path_item in (SPEC.get("paths") or {}).items():
        for http_method, opdef in path_item.items():
            if http_method not in HTTP_METHODS:
                continue
            entry = naming.get(f"{http_method} {path}")
            if not entry:
                continue  # coverage test enforces naming completeness separately
            ops.append(Op(path, http_method, opdef, entry["class"], entry["method"]))
    return sorted(ops, key=lambda o: o.name)