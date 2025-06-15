# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RecordingPauseResponse", "Data", "DataData"]


class DataData(BaseModel):
    status: Optional[str] = None


class Data(BaseModel):
    data: Optional[DataData] = None


class RecordingPauseResponse(BaseModel):
    data: Optional[Data] = None
