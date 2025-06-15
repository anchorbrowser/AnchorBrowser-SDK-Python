# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExtensionDeleteResponse", "Data", "DataData"]


class DataData(BaseModel):
    status: Optional[str] = None


class Data(BaseModel):
    data: Optional[DataData] = None


class ExtensionDeleteResponse(BaseModel):
    data: Optional[Data] = None
