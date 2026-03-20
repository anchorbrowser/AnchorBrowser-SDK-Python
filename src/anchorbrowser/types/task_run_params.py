# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["TaskRunParams"]


class TaskRunParams(TypedDict, total=False):
    input_params: Required[Dict[str, str]]
    """Key-value pairs of input parameters for the task"""

    cleanup_sessions: bool
    """Whether to clean up sessions after execution"""

    identity_id: str
    """Optional identity ID to use for the task"""

    session_id: str
    """Optional session ID to run the task in"""
