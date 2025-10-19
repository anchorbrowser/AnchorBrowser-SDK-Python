# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationListResponse", "Data", "DataIntegration"]


class DataIntegration(BaseModel):
    id: Optional[str] = None
    """Unique integration ID"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the integration was created"""

    name: Optional[str] = None
    """Integration name"""

    path: Optional[str] = None
    """Storage path for the integration"""

    type: Optional[Literal["1PASSWORD"]] = None
    """The type of integration"""


class Data(BaseModel):
    integrations: Optional[List[DataIntegration]] = None


class IntegrationListResponse(BaseModel):
    data: Optional[Data] = None
