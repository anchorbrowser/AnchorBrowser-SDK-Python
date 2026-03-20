# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from anchorbrowser import Anchorbrowser, AsyncAnchorbrowser
from anchorbrowser.types import TaskRunResponse, TaskGenerateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate(self, client: Anchorbrowser) -> None:
        task = client.tasks.generate(
            description="Download a specific file from a URL",
            name="file-downloader",
            user_task="Create a task that downloads a specific file from a given URL.",
        )
        assert_matches_type(TaskGenerateResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_with_all_params(self, client: Anchorbrowser) -> None:
        task = client.tasks.generate(
            description="Download a specific file from a URL",
            name="file-downloader",
            user_task="Create a task that downloads a specific file from a given URL.",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input_schema=[
                {
                    "display_name": "URL",
                    "type": "string",
                    "default_value": "default_value",
                    "description": "URL of the file to download",
                    "required": True,
                },
                {
                    "display_name": "File Name",
                    "type": "string",
                    "default_value": "default_value",
                    "description": "Name of the file to download",
                    "required": True,
                },
            ],
            output_schema=[
                {
                    "display_name": "Success",
                    "type": "boolean",
                    "default_value": "default_value",
                    "description": "Whether the download succeeded",
                    "required": True,
                },
                {
                    "display_name": "Message",
                    "type": "string",
                    "default_value": "default_value",
                    "description": "Status or error message",
                    "required": True,
                },
            ],
            task_browser_default_configuration={
                "initial_url": "https://example.com",
                "live_view": {"read_only": True},
                "proxy": {
                    "active": True,
                    "city": "city",
                    "country_code": "af",
                    "region": "region",
                    "type": "anchor_proxy",
                },
                "recording": {"active": True},
                "timeout": {
                    "idle_timeout": 0,
                    "max_duration": 0,
                },
            },
        )
        assert_matches_type(TaskGenerateResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate(self, client: Anchorbrowser) -> None:
        response = client.tasks.with_raw_response.generate(
            description="Download a specific file from a URL",
            name="file-downloader",
            user_task="Create a task that downloads a specific file from a given URL.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskGenerateResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate(self, client: Anchorbrowser) -> None:
        with client.tasks.with_streaming_response.generate(
            description="Download a specific file from a URL",
            name="file-downloader",
            user_task="Create a task that downloads a specific file from a given URL.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskGenerateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Anchorbrowser) -> None:
        task = client.tasks.run(
            task_id="taskId",
            input_params={
                "File Name": "invoice-2026-02.pdf",
                "Operation": "extract_text",
            },
        )
        assert_matches_type(TaskRunResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Anchorbrowser) -> None:
        task = client.tasks.run(
            task_id="taskId",
            input_params={
                "File Name": "invoice-2026-02.pdf",
                "Operation": "extract_text",
            },
            cleanup_sessions=True,
            identity_id="identity_id",
            session_id="session_id",
        )
        assert_matches_type(TaskRunResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Anchorbrowser) -> None:
        response = client.tasks.with_raw_response.run(
            task_id="taskId",
            input_params={
                "File Name": "invoice-2026-02.pdf",
                "Operation": "extract_text",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskRunResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Anchorbrowser) -> None:
        with client.tasks.with_streaming_response.run(
            task_id="taskId",
            input_params={
                "File Name": "invoice-2026-02.pdf",
                "Operation": "extract_text",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskRunResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_run(self, client: Anchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.with_raw_response.run(
                task_id="",
                input_params={
                    "File Name": "invoice-2026-02.pdf",
                    "Operation": "extract_text",
                },
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate(self, async_client: AsyncAnchorbrowser) -> None:
        task = await async_client.tasks.generate(
            description="Download a specific file from a URL",
            name="file-downloader",
            user_task="Create a task that downloads a specific file from a given URL.",
        )
        assert_matches_type(TaskGenerateResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncAnchorbrowser) -> None:
        task = await async_client.tasks.generate(
            description="Download a specific file from a URL",
            name="file-downloader",
            user_task="Create a task that downloads a specific file from a given URL.",
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input_schema=[
                {
                    "display_name": "URL",
                    "type": "string",
                    "default_value": "default_value",
                    "description": "URL of the file to download",
                    "required": True,
                },
                {
                    "display_name": "File Name",
                    "type": "string",
                    "default_value": "default_value",
                    "description": "Name of the file to download",
                    "required": True,
                },
            ],
            output_schema=[
                {
                    "display_name": "Success",
                    "type": "boolean",
                    "default_value": "default_value",
                    "description": "Whether the download succeeded",
                    "required": True,
                },
                {
                    "display_name": "Message",
                    "type": "string",
                    "default_value": "default_value",
                    "description": "Status or error message",
                    "required": True,
                },
            ],
            task_browser_default_configuration={
                "initial_url": "https://example.com",
                "live_view": {"read_only": True},
                "proxy": {
                    "active": True,
                    "city": "city",
                    "country_code": "af",
                    "region": "region",
                    "type": "anchor_proxy",
                },
                "recording": {"active": True},
                "timeout": {
                    "idle_timeout": 0,
                    "max_duration": 0,
                },
            },
        )
        assert_matches_type(TaskGenerateResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncAnchorbrowser) -> None:
        response = await async_client.tasks.with_raw_response.generate(
            description="Download a specific file from a URL",
            name="file-downloader",
            user_task="Create a task that downloads a specific file from a given URL.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskGenerateResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncAnchorbrowser) -> None:
        async with async_client.tasks.with_streaming_response.generate(
            description="Download a specific file from a URL",
            name="file-downloader",
            user_task="Create a task that downloads a specific file from a given URL.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskGenerateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncAnchorbrowser) -> None:
        task = await async_client.tasks.run(
            task_id="taskId",
            input_params={
                "File Name": "invoice-2026-02.pdf",
                "Operation": "extract_text",
            },
        )
        assert_matches_type(TaskRunResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncAnchorbrowser) -> None:
        task = await async_client.tasks.run(
            task_id="taskId",
            input_params={
                "File Name": "invoice-2026-02.pdf",
                "Operation": "extract_text",
            },
            cleanup_sessions=True,
            identity_id="identity_id",
            session_id="session_id",
        )
        assert_matches_type(TaskRunResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncAnchorbrowser) -> None:
        response = await async_client.tasks.with_raw_response.run(
            task_id="taskId",
            input_params={
                "File Name": "invoice-2026-02.pdf",
                "Operation": "extract_text",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskRunResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncAnchorbrowser) -> None:
        async with async_client.tasks.with_streaming_response.run(
            task_id="taskId",
            input_params={
                "File Name": "invoice-2026-02.pdf",
                "Operation": "extract_text",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskRunResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_run(self, async_client: AsyncAnchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.with_raw_response.run(
                task_id="",
                input_params={
                    "File Name": "invoice-2026-02.pdf",
                    "Operation": "extract_text",
                },
            )
