# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TaskGenerateResponse"]


class TaskGenerateResponse(BaseModel):
    """Response when task generation has been started (generation is asynchronous)."""

    id: str
    """The ID of the created task (use with generation-status and run endpoints)"""

    status: Literal["generating"]
    """Whether the task is still generating, ready to run, or failed."""
