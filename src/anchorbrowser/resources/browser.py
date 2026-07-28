from __future__ import annotations

from contextlib import _GeneratorContextManager, _AsyncGeneratorContextManager

from playwright.sync_api import Browser
from playwright.async_api import Browser as AsyncBrowser

from .._resource import SyncAPIResource, AsyncAPIResource
from ..lib.browser import (
    get_playwright_chromium_from_cdp_url,
    get_async_playwright_chromium_from_cdp_url,
)

__all__ = ["BrowserResource", "AsyncBrowserResource"]


class BrowserResource(SyncAPIResource):
    def connect(self, session_id: str) -> _GeneratorContextManager[Browser]:
        """Connect to a browser session.

        Args:
            session_id (str): The ID of the session to connect to.

        Returns:
            BrowserContext: a context manager that can be used to interact with the browser(playwright)
        """
        return get_playwright_chromium_from_cdp_url(str(self._client.base_url), session_id, self._client.api_key)

    def create(self) -> _GeneratorContextManager[Browser]:
        session = self._client.sessions.create_session()
        if not session.data or not session.data.id:
            raise ValueError("Failed to create session")
        return get_playwright_chromium_from_cdp_url(str(self._client.base_url), session.data.id, self._client.api_key)


class AsyncBrowserResource(AsyncAPIResource):
    async def connect(self, session_id: str) -> _AsyncGeneratorContextManager[AsyncBrowser]:
        """Connect to a browser session.

        Args:
            session_id (str): The ID of the session to connect to.

        Returns:
            BrowserContext: a context manager that can be used to interact with the browser(playwright)
        """
        return get_async_playwright_chromium_from_cdp_url(str(self._client.base_url), session_id, self._client.api_key)

    async def create(self) -> _AsyncGeneratorContextManager[AsyncBrowser]:
        """Create a new browser session.

        Returns:
            BrowserContext: a context manager that can be used to interact with the browser(playwright)
        """
        session = await self._client.sessions.create_session()
        if not session.data or not session.data.id:
            raise ValueError("Failed to create session")
        return get_async_playwright_chromium_from_cdp_url(
            str(self._client.base_url), session.data.id, self._client.api_key
        )
