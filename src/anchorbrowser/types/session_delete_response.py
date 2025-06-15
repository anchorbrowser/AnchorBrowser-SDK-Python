# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SessionDeleteResponse", "Data"]


class Data(BaseModel):
    status: Optional[str] = None


class SessionDeleteResponse(BaseModel):
    data: Optional[Data] = None
