# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ...types import task_run_params, task_generate_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .generations import (
    GenerationsResource,
    AsyncGenerationsResource,
    GenerationsResourceWithRawResponse,
    AsyncGenerationsResourceWithRawResponse,
    GenerationsResourceWithStreamingResponse,
    AsyncGenerationsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.task_run_response import TaskRunResponse
from ...types.task_generate_response import TaskGenerateResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def generations(self) -> GenerationsResource:
        return GenerationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/anchorbrowser/AnchorBrowser-SDK-Python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/anchorbrowser/AnchorBrowser-SDK-Python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def generate(
        self,
        *,
        description: str,
        name: str,
        user_task: str,
        application_id: str | Omit = omit,
        input_schema: Iterable[task_generate_params.InputSchema] | Omit = omit,
        output_schema: Iterable[task_generate_params.OutputSchema] | Omit = omit,
        task_browser_default_configuration: task_generate_params.TaskBrowserDefaultConfiguration | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGenerateResponse:
        """Initiates asynchronous task generation.

        Use the returned task ID to poll for
        completion, then execute the task.

        Args:
          description: Description of the task

          name: Name of the task

          user_task: Natural language description of what the task should do (used for AI generation)

          application_id: Optional application (connection) ID to associate with the task

          input_schema: Optional list of input parameters for the task. Defaults to empty array.

          output_schema: Optional list of output parameters for the task. Defaults to empty array.

          task_browser_default_configuration: Optional default browser/session configuration when running this task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/tasks/generate",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "user_task": user_task,
                    "application_id": application_id,
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                    "task_browser_default_configuration": task_browser_default_configuration,
                },
                task_generate_params.TaskGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGenerateResponse,
        )

    def run(
        self,
        task_id: str,
        *,
        input_params: Dict[str, str],
        cleanup_sessions: bool | Omit = omit,
        identity_id: str | Omit = omit,
        session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRunResponse:
        """
        Triggers execution of a task by ID using the V2 tasks API.

        Args:
          input_params: Key-value pairs of input parameters for the task

          cleanup_sessions: Whether to clean up sessions after execution (default: true)

          identity_id: Optional identity ID to use for the task

          session_id: Optional session ID to run the task in

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._post(
            path_template("/v2/tasks/{task_id}/run", task_id=task_id),
            body=maybe_transform(
                {
                    "input_params": input_params,
                    "cleanup_sessions": cleanup_sessions,
                    "identity_id": identity_id,
                    "session_id": session_id,
                },
                task_run_params.TaskRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRunResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def generations(self) -> AsyncGenerationsResource:
        return AsyncGenerationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/anchorbrowser/AnchorBrowser-SDK-Python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/anchorbrowser/AnchorBrowser-SDK-Python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def generate(
        self,
        *,
        description: str,
        name: str,
        user_task: str,
        application_id: str | Omit = omit,
        input_schema: Iterable[task_generate_params.InputSchema] | Omit = omit,
        output_schema: Iterable[task_generate_params.OutputSchema] | Omit = omit,
        task_browser_default_configuration: task_generate_params.TaskBrowserDefaultConfiguration | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGenerateResponse:
        """Initiates asynchronous task generation.

        Use the returned task ID to poll for
        completion, then execute the task.

        Args:
          description: Description of the task

          name: Name of the task

          user_task: Natural language description of what the task should do (used for AI generation)

          application_id: Optional application (connection) ID to associate with the task

          input_schema: Optional list of input parameters for the task. Defaults to empty array.

          output_schema: Optional list of output parameters for the task. Defaults to empty array.

          task_browser_default_configuration: Optional default browser/session configuration when running this task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/tasks/generate",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "user_task": user_task,
                    "application_id": application_id,
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                    "task_browser_default_configuration": task_browser_default_configuration,
                },
                task_generate_params.TaskGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGenerateResponse,
        )

    async def run(
        self,
        task_id: str,
        *,
        input_params: Dict[str, str],
        cleanup_sessions: bool | Omit = omit,
        identity_id: str | Omit = omit,
        session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRunResponse:
        """
        Triggers execution of a task by ID using the V2 tasks API.

        Args:
          input_params: Key-value pairs of input parameters for the task

          cleanup_sessions: Whether to clean up sessions after execution (default: true)

          identity_id: Optional identity ID to use for the task

          session_id: Optional session ID to run the task in

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._post(
            path_template("/v2/tasks/{task_id}/run", task_id=task_id),
            body=await async_maybe_transform(
                {
                    "input_params": input_params,
                    "cleanup_sessions": cleanup_sessions,
                    "identity_id": identity_id,
                    "session_id": session_id,
                },
                task_run_params.TaskRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRunResponse,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.generate = to_raw_response_wrapper(
            tasks.generate,
        )
        self.run = to_raw_response_wrapper(
            tasks.run,
        )

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._tasks.runs)

    @cached_property
    def generations(self) -> GenerationsResourceWithRawResponse:
        return GenerationsResourceWithRawResponse(self._tasks.generations)


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.generate = async_to_raw_response_wrapper(
            tasks.generate,
        )
        self.run = async_to_raw_response_wrapper(
            tasks.run,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._tasks.runs)

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithRawResponse:
        return AsyncGenerationsResourceWithRawResponse(self._tasks.generations)


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.generate = to_streamed_response_wrapper(
            tasks.generate,
        )
        self.run = to_streamed_response_wrapper(
            tasks.run,
        )

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._tasks.runs)

    @cached_property
    def generations(self) -> GenerationsResourceWithStreamingResponse:
        return GenerationsResourceWithStreamingResponse(self._tasks.generations)


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.generate = async_to_streamed_response_wrapper(
            tasks.generate,
        )
        self.run = async_to_streamed_response_wrapper(
            tasks.run,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._tasks.runs)

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithStreamingResponse:
        return AsyncGenerationsResourceWithStreamingResponse(self._tasks.generations)
