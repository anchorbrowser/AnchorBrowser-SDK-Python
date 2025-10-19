# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["IntegrationDeleteResponse", "Data", "DataIntegration"]


class DataIntegration(BaseModel):
    id: Optional[str] = None

    deleted: Optional[bool] = None

    path: Optional[str] = None


class Data(BaseModel):
    integration: Optional[DataIntegration] = None


class IntegrationDeleteResponse(BaseModel):
    data: Optional[Data] = None
