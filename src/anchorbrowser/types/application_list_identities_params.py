# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ApplicationListIdentitiesParams"]


class ApplicationListIdentitiesParams(TypedDict, total=False):
    metadata: str
    """Filter identities by metadata.

    Pass a **JSON object** to filter identities whose metadata contains the
    specified key-value pairs.
    """

    search: str
    """Search query to filter identities by name"""
