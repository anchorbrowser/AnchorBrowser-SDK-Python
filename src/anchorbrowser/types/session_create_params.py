# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "SessionCreateParams",
    "Browser",
    "BrowserAdblock",
    "BrowserCaptchaSolver",
    "BrowserDisableWebSecurity",
    "BrowserFullscreen",
    "BrowserHeadless",
    "BrowserP2pDownload",
    "BrowserPopupBlocker",
    "BrowserProfile",
    "BrowserViewport",
    "Session",
    "SessionLiveView",
    "SessionProxy",
    "SessionProxyAnchorProxy",
    "SessionProxyCustomProxy",
    "SessionRecording",
    "SessionTimeout",
]


class SessionCreateParams(TypedDict, total=False):
    browser: Browser
    """Browser-specific configurations."""

    session: Session
    """Session-related configurations."""


class BrowserAdblock(TypedDict, total=False):
    active: bool
    """Enable or disable ad-blocking. Defaults to `true`."""


class BrowserCaptchaSolver(TypedDict, total=False):
    active: bool
    """Enable or disable captcha-solving.

    Requires proxy to be active. Defaults to `false`.
    """


class BrowserDisableWebSecurity(TypedDict, total=False):
    active: bool
    """Whether to disable web security features (CORS, same-origin policy, etc.).

    Allows accessing iframes and resources from different origins. Defaults to
    `false`.
    """


class BrowserFullscreen(TypedDict, total=False):
    active: bool
    """Enable or disable fullscreen mode.

    When enabled, the browser will start in fullscreen mode. Defaults to `false`.
    """


class BrowserHeadless(TypedDict, total=False):
    active: bool
    """Whether browser should be headless or headful. Defaults to `false`."""


class BrowserP2pDownload(TypedDict, total=False):
    active: bool
    """Enable or disable P2P downloads.

    When enabled, the browser will capture downloads for direct data extraction,
    instead of uploading them on Anchor's storage. Defaults to `false`.
    """


class BrowserPopupBlocker(TypedDict, total=False):
    active: bool
    """Blocks popups, including ads and CAPTCHA consent banners.

    Requires adblock to be active. Defaults to `true`.
    """


class BrowserProfile(TypedDict, total=False):
    name: str
    """The name of the profile to be used during the browser session."""

    persist: bool
    """
    Indicates whether the browser session profile data should be saved when the
    browser session ends. Defaults to `false`.
    """

    reset_preferences: bool
    """When enabled, resets the profile's preferences on session creation.

    Defaults to `false`.
    """


class BrowserViewport(TypedDict, total=False):
    height: int
    """Height of the viewport in pixels. Defaults to `900`."""

    width: int
    """Width of the viewport in pixels. Defaults to `1440`."""


class Browser(TypedDict, total=False):
    adblock: BrowserAdblock
    """Configuration for ad-blocking."""

    captcha_solver: BrowserCaptchaSolver
    """Configuration for captcha-solving."""

    disable_web_security: BrowserDisableWebSecurity
    """Configuration for disabling web security features."""

    extensions: List[str]
    """Array of extension IDs to load in the browser session.

    Extensions must be previously uploaded using the Extensions API.
    """

    fullscreen: BrowserFullscreen
    """Configuration for fullscreen mode."""

    headless: BrowserHeadless
    """Configuration for headless mode."""

    p2p_download: BrowserP2pDownload
    """Configuration for peer-to-peer download capture functionality."""

    popup_blocker: BrowserPopupBlocker
    """Configuration for popup blocking."""

    profile: BrowserProfile
    """Options for managing and persisting browser session profiles."""

    viewport: BrowserViewport
    """Configuration for the browser's viewport size."""


class SessionLiveView(TypedDict, total=False):
    read_only: bool
    """Enable or disable read-only mode for live viewing. Defaults to `false`."""


class SessionProxyAnchorProxy(TypedDict, total=False):
    active: Required[bool]

    country_code: Literal[
        "af",
        "al",
        "dz",
        "ad",
        "ao",
        "ag",
        "ar",
        "am",
        "aw",
        "au",
        "at",
        "az",
        "bs",
        "bh",
        "bd",
        "bb",
        "by",
        "be",
        "bz",
        "bj",
        "bm",
        "bo",
        "ba",
        "bw",
        "br",
        "bn",
        "bg",
        "bf",
        "bi",
        "kh",
        "cm",
        "ca",
        "cv",
        "td",
        "cl",
        "cn",
        "co",
        "cg",
        "cr",
        "ci",
        "hr",
        "cu",
        "cy",
        "cz",
        "dk",
        "dj",
        "dm",
        "do",
        "ec",
        "eg",
        "sv",
        "gq",
        "ee",
        "sz",
        "et",
        "fj",
        "fi",
        "fr",
        "pf",
        "ga",
        "gm",
        "ge",
        "de",
        "gh",
        "gr",
        "gd",
        "gt",
        "gn",
        "gy",
        "ht",
        "hn",
        "hk",
        "hu",
        "is",
        "in",
        "id",
        "ir",
        "iq",
        "ie",
        "il",
        "it",
        "jm",
        "jp",
        "jo",
        "kz",
        "ke",
        "kw",
        "kg",
        "la",
        "lv",
        "lb",
        "ls",
        "lr",
        "ly",
        "lt",
        "lu",
        "mk",
        "mg",
        "mw",
        "my",
        "mv",
        "ml",
        "mt",
        "mr",
        "mx",
        "md",
        "mn",
        "me",
        "ma",
        "mz",
        "mm",
        "na",
        "np",
        "nl",
        "nc",
        "nz",
        "ni",
        "ne",
        "ng",
        "no",
        "om",
        "pk",
        "pa",
        "pg",
        "py",
        "pe",
        "ph",
        "pl",
        "pt",
        "pr",
        "qa",
        "ro",
        "ru",
        "rw",
        "lc",
        "ws",
        "sm",
        "sa",
        "sn",
        "rs",
        "sl",
        "sg",
        "sk",
        "si",
        "so",
        "za",
        "kr",
        "ss",
        "es",
        "lk",
        "sd",
        "sr",
        "se",
        "ch",
        "sy",
        "st",
        "tw",
        "tj",
        "tz",
        "th",
        "tl",
        "tr",
        "tg",
        "tt",
        "tn",
        "tm",
        "ug",
        "ua",
        "gb",
        "us",
        "uy",
        "uz",
        "vu",
        "ve",
        "vn",
        "ye",
        "zm",
        "zw",
        "bt",
        "gw",
        "mu",
        "ae",
        "as",
        "fo",
        "gf",
        "gi",
        "gp",
        "gg",
        "li",
        "mq",
        "mc",
        "sc",
        "tc",
    ]
    """Supported country codes ISO 2 lowercase

    **On change make sure to update the Proxy type.**
    """

    type: Literal["anchor_residential", "anchor_mobile", "anchor_gov"]
    """**On change make sure to update the country_code.**"""


class SessionProxyCustomProxy(TypedDict, total=False):
    active: Required[bool]

    password: Required[str]
    """Proxy password"""

    server: Required[str]
    """Proxy server address"""

    type: Required[Literal["custom"]]

    username: Required[str]
    """Proxy username"""


SessionProxy: TypeAlias = Union[SessionProxyAnchorProxy, SessionProxyCustomProxy]


class SessionRecording(TypedDict, total=False):
    active: bool
    """Enable or disable video recording of the browser session. Defaults to `true`."""


class SessionTimeout(TypedDict, total=False):
    idle_timeout: int
    """
    The amount of time (in minutes) the browser session waits for new connections
    after all others are closed before stopping. Defaults to `5`.
    """

    max_duration: int
    """Maximum amount of time (in minutes) for the browser to run before terminating.

    Defaults to `20`.
    """


class Session(TypedDict, total=False):
    initial_url: str
    """The URL to navigate to when the browser session starts.

    If not provided, the browser will load an empty page.
    """

    live_view: SessionLiveView
    """Configuration for live viewing the browser session."""

    proxy: SessionProxy
    """Proxy Documentation available at [Proxy Documentation](/advanced/proxy)"""

    recording: SessionRecording
    """Configuration for session recording."""

    timeout: SessionTimeout
    """Timeout configurations for the browser session."""
