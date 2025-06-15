# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AllRetrieveStatusResponse", "Data", "DataItem"]


class DataItem(BaseModel):
    created_at: datetime
    """Timestamp when the browser session was created"""

    session_id: str
    """Unique identifier for the browser session"""

    status: str
    """Current status of the browser session"""


class Data(BaseModel):
    count: Optional[int] = None
    """Total number of browser sessions"""

    items: Optional[List[DataItem]] = None


class AllRetrieveStatusResponse(BaseModel):
    data: Optional[Data] = None
