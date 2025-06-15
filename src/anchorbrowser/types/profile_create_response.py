# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ProfileCreateResponse", "Data"]


class Data(BaseModel):
    status: Optional[str] = None


class ProfileCreateResponse(BaseModel):
    data: Optional[Data] = None
