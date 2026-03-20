# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GenerationGetStatusResponse"]


class GenerationGetStatusResponse(BaseModel):
    """Current status of asynchronous task generation."""

    id: str
    """The task ID"""

    status: Literal["generating", "ready", "failed"]
    """Whether the task is still generating, ready to run, or failed."""

    error: Optional[str] = None
    """Error message when status is failed"""

    project_state: Optional[str] = None
    """Optional internal project state"""
