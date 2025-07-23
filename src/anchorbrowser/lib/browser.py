from typing import TYPE_CHECKING, Any, Dict, Callable, Optional, TypedDict
from contextlib import contextmanager, asynccontextmanager

from pydantic import BaseModel

if TYPE_CHECKING:
    from playwright.sync_api import Worker, BrowserContext
    from playwright.async_api import Worker as AsyncWorker, BrowserContext as AsyncBrowserContext


@contextmanager
def get_playwright_chromium_from_cdp_url(api_base_url: str, session_id: str, api_key: str):
    from playwright.sync_api import sync_playwright

    browser = None
    playwright = sync_playwright().start()
    try:
        browser = playwright.chromium.connect_over_cdp(get_cdp_url(api_base_url, session_id, api_key))
        yield browser
    finally:
        if browser:
            browser.close()
        playwright.stop()


@asynccontextmanager
async def get_async_playwright_chromium_from_cdp_url(api_base_url: str, session_id: str, api_key: str):
    from playwright.async_api import async_playwright

    browser = None
    playwright = await async_playwright().start()
    try:
        browser = await playwright.chromium.connect_over_cdp(get_cdp_url(api_base_url, session_id, api_key))
        yield browser
    finally:
        if browser:
            await browser.close()
        await playwright.stop()


def get_cdp_url(api_base_url: str, session_id: str, api_key: str):
    return f"{api_base_url.replace('https://', 'wss://').replace('api.', 'connect.')}?apiKey={api_key}&sessionId={session_id}"


def get_agent_ws_url(api_base_url: str, session_id: str):
    return f"{api_base_url.replace('https://', 'wss://').replace('api.', 'connect.')}/ws?sessionId={session_id}"


def get_ai_service_worker(browser_context: "BrowserContext") -> Optional["Worker"]:
    return next(
        (
            sw
            for sw in browser_context.service_workers
            if "chrome-extension://bppehibnhionalpjigdjdilknbljaeai/background.js" in sw.url
        ),
        None,
    )


async def get_ai_service_worker_async(browser_context: "AsyncBrowserContext") -> Optional["AsyncWorker"]:
    return next(
        (
            sw
            for sw in browser_context.service_workers
            if "chrome-extension://bppehibnhionalpjigdjdilknbljaeai/background.js" in sw.url
        ),
        None,
    )


class BrowserSetup(BaseModel):
    session_id: str
    base_url: str
    api_key: str
    _browser = None
    _async_browser = None
    _context_manager = None
    _async_context_manager = None

    async def __aenter__(self):
        self._async_context_manager = get_async_playwright_chromium_from_cdp_url(
            self.base_url,
            self.session_id,
            self.api_key,
        )
        self._async_browser = await self._async_context_manager.__aenter__()
        return self

    def __enter__(self):
        self._context_manager = get_playwright_chromium_from_cdp_url(
            self.base_url,
            self.session_id,
            self.api_key,
        )
        self._browser = self._context_manager.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        if self._context_manager:
            return self._context_manager.__exit__(exc_type, exc_val, exc_tb)

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        if self._async_context_manager:
            return await self._async_context_manager.__aexit__(exc_type, exc_val, exc_tb)

    @property
    def browser_generator(self):
        return get_playwright_chromium_from_cdp_url(
            self.base_url,
            self.session_id,
            self.api_key,
        )

    @property
    def async_browser_generator(self):
        return get_async_playwright_chromium_from_cdp_url(
            self.base_url,
            self.session_id,
            self.api_key,
        )

    @property
    def browser(self):
        if self._browser is None:
            raise RuntimeError("BrowserSetup must be used as a context manager")
        return self._browser

    @property
    async def async_browser(self):
        if self._async_browser is None:
            raise RuntimeError("BrowserSetup must be used as a context manager")
        return self._async_browser

    @property
    def context(self):
        return self.browser.contexts[0]

    @property
    async def async_context(self):
        return (await self.async_browser).contexts[0]

    @property
    def page(self):
        return self.context.pages[0]

    @property
    async def async_page(self):
        return (await self.async_context).pages[0]

    @property
    def ai(self):
        ai_service_worker = get_ai_service_worker(self.context)
        if not ai_service_worker:
            raise ValueError("AI service worker not found")
        return ai_service_worker

    @property
    async def async_ai(self):
        ai_service_worker = await get_ai_service_worker_async(await self.async_context)
        if not ai_service_worker:
            raise ValueError("AI service worker not found")
        return ai_service_worker


class AgentTaskParams(TypedDict, total=False):
    url: Optional[str]
    output_schema: Optional[Dict[str, Any]]
    on_agent_step: Optional[Callable[[str], None]]


class BrowserTaskResponse(TypedDict):
    session_id: str
    task_result_task: Any
    playwright_browser: Any
