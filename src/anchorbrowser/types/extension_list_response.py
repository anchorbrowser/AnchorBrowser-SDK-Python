# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExtensionListResponse", "Data", "DataManifest"]


class DataManifest(BaseModel):
    description: Optional[str] = None

    manifest_version: Optional[int] = None

    name: Optional[str] = None

    permissions: Optional[List[str]] = None

    version: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the extension"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the extension was created"""

    manifest: Optional[DataManifest] = None

    name: Optional[str] = None
    """Extension name"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp when the extension was last updated"""


class ExtensionListResponse(BaseModel):
    data: Optional[List[Data]] = None
