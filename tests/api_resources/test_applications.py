# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from anchorbrowser import Anchorbrowser, AsyncAnchorbrowser
from anchorbrowser.types import (
    ApplicationListResponse,
    ApplicationCreateResponse,
    ApplicationDeleteResponse,
    ApplicationRetrieveResponse,
    ApplicationListIdentitiesResponse,
    ApplicationCreateIdentityTokenResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApplications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Anchorbrowser) -> None:
        application = client.applications.create(
            source="https://example.com",
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Anchorbrowser) -> None:
        application = client.applications.create(
            source="https://example.com",
            description="An example application",
            name="Example App",
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Anchorbrowser) -> None:
        response = client.applications.with_raw_response.create(
            source="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Anchorbrowser) -> None:
        with client.applications.with_streaming_response.create(
            source="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationCreateResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Anchorbrowser) -> None:
        application = client.applications.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ApplicationRetrieveResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Anchorbrowser) -> None:
        response = client.applications.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationRetrieveResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Anchorbrowser) -> None:
        with client.applications.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationRetrieveResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Anchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Anchorbrowser) -> None:
        application = client.applications.list()
        assert_matches_type(ApplicationListResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Anchorbrowser) -> None:
        application = client.applications.list(
            search="search",
        )
        assert_matches_type(ApplicationListResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Anchorbrowser) -> None:
        response = client.applications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationListResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Anchorbrowser) -> None:
        with client.applications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationListResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Anchorbrowser) -> None:
        application = client.applications.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Anchorbrowser) -> None:
        response = client.applications.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Anchorbrowser) -> None:
        with client.applications.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Anchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_identity_token(self, client: Anchorbrowser) -> None:
        application = client.applications.create_identity_token(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            callback_url="https://example.com/auth/callback",
        )
        assert_matches_type(ApplicationCreateIdentityTokenResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_identity_token(self, client: Anchorbrowser) -> None:
        response = client.applications.with_raw_response.create_identity_token(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            callback_url="https://example.com/auth/callback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationCreateIdentityTokenResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_identity_token(self, client: Anchorbrowser) -> None:
        with client.applications.with_streaming_response.create_identity_token(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            callback_url="https://example.com/auth/callback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationCreateIdentityTokenResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_identity_token(self, client: Anchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.with_raw_response.create_identity_token(
                application_id="",
                callback_url="https://example.com/auth/callback",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_identities(self, client: Anchorbrowser) -> None:
        application = client.applications.list_identities(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ApplicationListIdentitiesResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_identities_with_all_params(self, client: Anchorbrowser) -> None:
        application = client.applications.list_identities(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata="metadata",
            search="search",
        )
        assert_matches_type(ApplicationListIdentitiesResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_identities(self, client: Anchorbrowser) -> None:
        response = client.applications.with_raw_response.list_identities(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationListIdentitiesResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_identities(self, client: Anchorbrowser) -> None:
        with client.applications.with_streaming_response.list_identities(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationListIdentitiesResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_identities(self, client: Anchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.with_raw_response.list_identities(
                application_id="",
            )


class TestAsyncApplications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAnchorbrowser) -> None:
        application = await async_client.applications.create(
            source="https://example.com",
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAnchorbrowser) -> None:
        application = await async_client.applications.create(
            source="https://example.com",
            description="An example application",
            name="Example App",
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAnchorbrowser) -> None:
        response = await async_client.applications.with_raw_response.create(
            source="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAnchorbrowser) -> None:
        async with async_client.applications.with_streaming_response.create(
            source="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationCreateResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAnchorbrowser) -> None:
        application = await async_client.applications.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ApplicationRetrieveResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAnchorbrowser) -> None:
        response = await async_client.applications.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationRetrieveResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAnchorbrowser) -> None:
        async with async_client.applications.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationRetrieveResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAnchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAnchorbrowser) -> None:
        application = await async_client.applications.list()
        assert_matches_type(ApplicationListResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAnchorbrowser) -> None:
        application = await async_client.applications.list(
            search="search",
        )
        assert_matches_type(ApplicationListResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAnchorbrowser) -> None:
        response = await async_client.applications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationListResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAnchorbrowser) -> None:
        async with async_client.applications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationListResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAnchorbrowser) -> None:
        application = await async_client.applications.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAnchorbrowser) -> None:
        response = await async_client.applications.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAnchorbrowser) -> None:
        async with async_client.applications.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAnchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_identity_token(self, async_client: AsyncAnchorbrowser) -> None:
        application = await async_client.applications.create_identity_token(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            callback_url="https://example.com/auth/callback",
        )
        assert_matches_type(ApplicationCreateIdentityTokenResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_identity_token(self, async_client: AsyncAnchorbrowser) -> None:
        response = await async_client.applications.with_raw_response.create_identity_token(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            callback_url="https://example.com/auth/callback",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationCreateIdentityTokenResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_identity_token(self, async_client: AsyncAnchorbrowser) -> None:
        async with async_client.applications.with_streaming_response.create_identity_token(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            callback_url="https://example.com/auth/callback",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationCreateIdentityTokenResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_identity_token(self, async_client: AsyncAnchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.with_raw_response.create_identity_token(
                application_id="",
                callback_url="https://example.com/auth/callback",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_identities(self, async_client: AsyncAnchorbrowser) -> None:
        application = await async_client.applications.list_identities(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ApplicationListIdentitiesResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_identities_with_all_params(self, async_client: AsyncAnchorbrowser) -> None:
        application = await async_client.applications.list_identities(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata="metadata",
            search="search",
        )
        assert_matches_type(ApplicationListIdentitiesResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_identities(self, async_client: AsyncAnchorbrowser) -> None:
        response = await async_client.applications.with_raw_response.list_identities(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationListIdentitiesResponse, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_identities(self, async_client: AsyncAnchorbrowser) -> None:
        async with async_client.applications.with_streaming_response.list_identities(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationListIdentitiesResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_identities(self, async_client: AsyncAnchorbrowser) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.with_raw_response.list_identities(
                application_id="",
            )
