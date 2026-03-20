# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from anchorbrowser import Anchorbrowser, AsyncAnchorbrowser
from anchorbrowser.types.tasks import GenerationGetStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: Anchorbrowser) -> None:
        generation = client.tasks.generations.get_status(
            "taskId",
        )
        assert_matches_type(GenerationGetStatusResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: Anchorbrowser) -> None:
        response = client.tasks.generations.with_raw_response.get_status(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(GenerationGetStatusResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: Anchorbrowser) -> None:
        with client.tasks.generations.with_streaming_response.get_status(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(GenerationGetStatusResponse, generation, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: Anchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.generations.with_raw_response.get_status(
                "",
            )


class TestAsyncGenerations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncAnchorbrowser) -> None:
        generation = await async_client.tasks.generations.get_status(
            "taskId",
        )
        assert_matches_type(GenerationGetStatusResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncAnchorbrowser) -> None:
        response = await async_client.tasks.generations.with_raw_response.get_status(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(GenerationGetStatusResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncAnchorbrowser) -> None:
        async with async_client.tasks.generations.with_streaming_response.get_status(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(GenerationGetStatusResponse, generation, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncAnchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.generations.with_raw_response.get_status(
                "",
            )
