# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from anchorbrowser import Anchorbrowser, AsyncAnchorbrowser

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Anchorbrowser) -> None:
        execution = client.task.executions.retrieve(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, execution, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Anchorbrowser) -> None:
        response = client.task.executions.with_raw_response.retrieve(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(object, execution, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Anchorbrowser) -> None:
        with client.task.executions.with_streaming_response.retrieve(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Anchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.task.executions.with_raw_response.retrieve(
                execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                task_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.task.executions.with_raw_response.retrieve(
                execution_id="",
                task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncExecutions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAnchorbrowser) -> None:
        execution = await async_client.task.executions.retrieve(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, execution, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAnchorbrowser) -> None:
        response = await async_client.task.executions.with_raw_response.retrieve(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(object, execution, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAnchorbrowser) -> None:
        async with async_client.task.executions.with_streaming_response.retrieve(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAnchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.task.executions.with_raw_response.retrieve(
                execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                task_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.task.executions.with_raw_response.retrieve(
                execution_id="",
                task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
