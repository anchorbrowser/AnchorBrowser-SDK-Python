# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from anchorbrowser import Anchorbrowser, AsyncAnchorbrowser
from anchorbrowser.types.sessions.agent import FileListResponse, FileUploadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Anchorbrowser) -> None:
        file = client.sessions.agent.files.list(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Anchorbrowser) -> None:
        response = client.sessions.agent.files.with_raw_response.list(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Anchorbrowser) -> None:
        with client.sessions.agent.files.with_streaming_response.list(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Anchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.agent.files.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_upload(self, client: Anchorbrowser) -> None:
        file = client.sessions.agent.files.upload(
            session_id="550e8400-e29b-41d4-a716-446655440000",
            file=b"raw file contents",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upload(self, client: Anchorbrowser) -> None:
        response = client.sessions.agent.files.with_raw_response.upload(
            session_id="550e8400-e29b-41d4-a716-446655440000",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upload(self, client: Anchorbrowser) -> None:
        with client.sessions.agent.files.with_streaming_response.upload(
            session_id="550e8400-e29b-41d4-a716-446655440000",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_upload(self, client: Anchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.agent.files.with_raw_response.upload(
                session_id="",
                file=b"raw file contents",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAnchorbrowser) -> None:
        file = await async_client.sessions.agent.files.list(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAnchorbrowser) -> None:
        response = await async_client.sessions.agent.files.with_raw_response.list(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAnchorbrowser) -> None:
        async with async_client.sessions.agent.files.with_streaming_response.list(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncAnchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.agent.files.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload(self, async_client: AsyncAnchorbrowser) -> None:
        file = await async_client.sessions.agent.files.upload(
            session_id="550e8400-e29b-41d4-a716-446655440000",
            file=b"raw file contents",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncAnchorbrowser) -> None:
        response = await async_client.sessions.agent.files.with_raw_response.upload(
            session_id="550e8400-e29b-41d4-a716-446655440000",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncAnchorbrowser) -> None:
        async with async_client.sessions.agent.files.with_streaming_response.upload(
            session_id="550e8400-e29b-41d4-a716-446655440000",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncAnchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.agent.files.with_raw_response.upload(
                session_id="",
                file=b"raw file contents",
            )
