# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ApplicationCreateIdentityTokenResponse"]


class ApplicationCreateIdentityTokenResponse(BaseModel):
    token: str
    """The generated identity token for authentication"""

    expires_at: datetime = FieldInfo(alias="expiresAt")
    """The timestamp when the token expires"""

    token_hash: str = FieldInfo(alias="tokenHash")
    """A hash of the token for verification purposes"""
