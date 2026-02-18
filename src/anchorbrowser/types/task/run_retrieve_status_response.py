# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RunRetrieveStatusResponse"]


class RunRetrieveStatusResponse(BaseModel):
    run_id: str
    """The ID of the task run"""

    status: Literal["queued", "running", "success", "failure", "timeout", "cancelled"]
    """Current task run status"""

    error: Optional[str] = None
    """Error message when the run fails"""

    result: Optional[Dict[str, object]] = None
    """Task output when available"""

    session_id: Optional[str] = None
    """Session ID used for this task run"""
