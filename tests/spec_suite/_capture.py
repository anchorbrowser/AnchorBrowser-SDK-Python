"""Local capture HTTP server + request normalization shared by the wire-parity
test suite and scripts/update-wire-golden."""

from __future__ import annotations

import re
import json
import threading
from typing import Any
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlsplit, parse_qsl
from typing_extensions import override

from ._synth import all_operations

VALUE_HEADERS = {"anchor-api-key", "accept", "content-type"}
IGNORED_HEADERS = {"host", "connection", "content-length", "accept-encoding", "keep-alive"}


class CaptureServer:
    def __init__(self) -> None:
        self.captured: list[dict[str, Any]] = []
        routes = {
            (op.http_method, re.sub(r"\{[^}]+\}", "[^/]+", op.path)): op.success_content_type()
            for op in all_operations()
        }
        outer = self

        class Handler(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def _content_type_for(self, method: str, path: str) -> str:
                for (m, pattern), ctype in routes.items():
                    if m == method.lower() and re.fullmatch(pattern, path):
                        return ctype
                return "application/json"

            def _handle(self) -> None:
                length = int(self.headers.get("Content-Length") or 0)
                raw = self.rfile.read(length) if length else b""
                url = urlsplit(self.path)
                outer.captured.append(
                    {
                        "method": self.command,
                        "path": url.path,
                        "query": dict(parse_qsl(url.query)),
                        "headers": {k.lower(): v for k, v in self.headers.items()},
                        "body": raw,
                    }
                )
                ctype = self._content_type_for(self.command, url.path)
                if "json" in ctype:
                    payload = b'{"data": {}}'
                elif ctype.startswith("text/"):
                    payload = b"ok"
                else:
                    payload = b"\x89PNG"
                self.send_response(200)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            do_GET = do_POST = do_PUT = do_DELETE = do_PATCH = _handle

            @override
            def log_message(self, format: str, *args: Any) -> None:
                pass

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.server.daemon_threads = True
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    @property
    def base_url(self) -> str:
        return f"http://127.0.0.1:{self.server.server_port}"

    def stop(self) -> None:
        self.server.shutdown()


def normalize(req: dict[str, Any]) -> dict[str, Any]:
    """Reduce a captured request to its wire-meaningful, version-stable parts."""
    headers = req["headers"]
    content_type = headers.get("content-type", "")
    boundary = None
    m = re.search(r"boundary=(\S+)", content_type)
    if m:
        boundary = m.group(1)

    header_names = sorted(
        k for k in headers if k not in IGNORED_HEADERS and not k.startswith("x-stainless")
    )
    header_values = {}
    for k in header_names:
        if k in VALUE_HEADERS:
            v = headers[k]
            if boundary:
                v = v.replace(boundary, "<boundary>")
            header_values[k] = v

    body: Any = None
    raw: bytes = req["body"]
    if raw:
        if boundary:
            body = raw.decode(errors="replace").replace(boundary, "<boundary>").replace("\r\n", "\n").rstrip()
        elif "json" in content_type:
            body = json.loads(raw)
        else:
            body = raw.decode(errors="replace")

    return {
        "method": req["method"],
        "path": req["path"],
        "query": req["query"],
        "header_names": header_names,
        "headers": header_values,
        "body": body,
    }


def invoke(client: Any, op: Any) -> Any:
    resource = getattr(client, op.py_attr)
    method = getattr(resource, op.py_method)
    args, kwargs = op.build_kwargs()
    return method(*args, **kwargs)
