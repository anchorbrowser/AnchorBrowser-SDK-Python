# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/anchorbrowser/AnchorBrowser-SDK-Python#accessing-raw-response-data-eg-headers
        """
        return AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/anchorbrowser/AnchorBrowser-SDK-Python#with_streaming_response
        """
        return AgentResourceWithStreamingResponse(self)


class AsyncAgentResource(AsyncAPIResource):
    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/anchorbrowser/AnchorBrowser-SDK-Python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/anchorbrowser/AnchorBrowser-SDK-Python#with_streaming_response
        """
        return AsyncAgentResourceWithStreamingResponse(self)


class AgentResourceWithRawResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._agent.files)


class AsyncAgentResourceWithRawResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._agent.files)


class AgentResourceWithStreamingResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._agent.files)


class AsyncAgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._agent.files)
