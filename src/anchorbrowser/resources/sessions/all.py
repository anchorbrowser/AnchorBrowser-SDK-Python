# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.sessions.all_delete_all_response import AllDeleteAllResponse
from ...types.sessions.all_retrieve_status_response import AllRetrieveStatusResponse

__all__ = ["AllResource", "AsyncAllResource"]


class AllResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AllResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/anchorbrowser-python#accessing-raw-response-data-eg-headers
        """
        return AllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AllResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/anchorbrowser-python#with_streaming_response
        """
        return AllResourceWithStreamingResponse(self)

    def delete_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllDeleteAllResponse:
        """Terminates all active browser sessions associated with the provided API key."""
        return self._delete(
            "/v1/sessions/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllDeleteAllResponse,
        )

    def retrieve_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllRetrieveStatusResponse:
        """
        Retrieves status information for all browser sessions associated with the API
        key.
        """
        return self._get(
            "/v1/sessions/all/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllRetrieveStatusResponse,
        )


class AsyncAllResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAllResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/anchorbrowser-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAllResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/anchorbrowser-python#with_streaming_response
        """
        return AsyncAllResourceWithStreamingResponse(self)

    async def delete_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllDeleteAllResponse:
        """Terminates all active browser sessions associated with the provided API key."""
        return await self._delete(
            "/v1/sessions/all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllDeleteAllResponse,
        )

    async def retrieve_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllRetrieveStatusResponse:
        """
        Retrieves status information for all browser sessions associated with the API
        key.
        """
        return await self._get(
            "/v1/sessions/all/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllRetrieveStatusResponse,
        )


class AllResourceWithRawResponse:
    def __init__(self, all: AllResource) -> None:
        self._all = all

        self.delete_all = to_raw_response_wrapper(
            all.delete_all,
        )
        self.retrieve_status = to_raw_response_wrapper(
            all.retrieve_status,
        )


class AsyncAllResourceWithRawResponse:
    def __init__(self, all: AsyncAllResource) -> None:
        self._all = all

        self.delete_all = async_to_raw_response_wrapper(
            all.delete_all,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            all.retrieve_status,
        )


class AllResourceWithStreamingResponse:
    def __init__(self, all: AllResource) -> None:
        self._all = all

        self.delete_all = to_streamed_response_wrapper(
            all.delete_all,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            all.retrieve_status,
        )


class AsyncAllResourceWithStreamingResponse:
    def __init__(self, all: AsyncAllResource) -> None:
        self._all = all

        self.delete_all = async_to_streamed_response_wrapper(
            all.delete_all,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            all.retrieve_status,
        )
