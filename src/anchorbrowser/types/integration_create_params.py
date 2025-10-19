# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IntegrationCreateParams", "Credentials", "CredentialsData"]


class IntegrationCreateParams(TypedDict, total=False):
    credentials: Required[Credentials]

    name: Required[str]
    """Name for the integration"""

    type: Required[Literal["1PASSWORD"]]
    """The type of integration"""


class CredentialsData(TypedDict, total=False):
    service_account: Required[Annotated[str, PropertyInfo(alias="serviceAccount")]]
    """Service account token"""


class Credentials(TypedDict, total=False):
    data: Required[CredentialsData]

    type: Required[Literal["serviceAccount"]]
    """Credential type"""
