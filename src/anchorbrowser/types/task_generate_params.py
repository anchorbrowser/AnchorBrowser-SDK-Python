# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "TaskGenerateParams",
    "InputSchema",
    "OutputSchema",
    "TaskBrowserDefaultConfiguration",
    "TaskBrowserDefaultConfigurationLiveView",
    "TaskBrowserDefaultConfigurationProxy",
    "TaskBrowserDefaultConfigurationProxyAnchorProxy",
    "TaskBrowserDefaultConfigurationProxyCustomProxy",
    "TaskBrowserDefaultConfigurationRecording",
    "TaskBrowserDefaultConfigurationTimeout",
]


class TaskGenerateParams(TypedDict, total=False):
    description: Required[str]
    """Description of the task"""

    name: Required[str]
    """Name of the task"""

    user_task: Required[str]
    """
    Natural language description of what the task should do (used for AI generation)
    """

    application_id: str
    """Optional application (connection) ID to associate with the task"""

    input_schema: Iterable[InputSchema]
    """Optional list of input parameters for the task. Defaults to empty array."""

    output_schema: Iterable[OutputSchema]
    """Optional list of output parameters for the task. Defaults to empty array."""

    task_browser_default_configuration: TaskBrowserDefaultConfiguration
    """Optional default browser/session configuration when running this task"""


class InputSchema(TypedDict, total=False):
    """A single input or output parameter for a generated task."""

    display_name: Required[str]
    """Human-readable name for the parameter"""

    type: Required[Literal["string", "number", "boolean", "date"]]
    """Data type of the parameter"""

    default_value: str
    """Optional default value as a string"""

    description: str
    """Optional description of the parameter"""

    required: bool
    """Whether the parameter is required"""


class OutputSchema(TypedDict, total=False):
    """A single input or output parameter for a generated task."""

    display_name: Required[str]
    """Human-readable name for the parameter"""

    type: Required[Literal["string", "number", "boolean", "date"]]
    """Data type of the parameter"""

    default_value: str
    """Optional default value as a string"""

    description: str
    """Optional description of the parameter"""

    required: bool
    """Whether the parameter is required"""


class TaskBrowserDefaultConfigurationLiveView(TypedDict, total=False):
    """Configuration for live viewing the browser session."""

    read_only: bool
    """Enable or disable read-only mode for live viewing. Defaults to `false`."""


class TaskBrowserDefaultConfigurationProxyAnchorProxy(TypedDict, total=False):
    active: Required[bool]

    city: str
    """City name for precise geographic targeting.

    Supported for anchor_proxy only. Can only be used when region is also provided.
    """

    country_code: Literal[
        "af",
        "al",
        "dz",
        "ad",
        "ao",
        "as",
        "ag",
        "ar",
        "am",
        "aw",
        "au",
        "at",
        "az",
        "bs",
        "bh",
        "bb",
        "by",
        "be",
        "bz",
        "bj",
        "bm",
        "bo",
        "ba",
        "br",
        "bg",
        "bf",
        "cm",
        "ca",
        "cv",
        "td",
        "cl",
        "co",
        "cg",
        "cr",
        "ci",
        "hr",
        "cu",
        "cy",
        "cz",
        "dk",
        "dm",
        "do",
        "ec",
        "eg",
        "sv",
        "ee",
        "et",
        "fo",
        "fi",
        "fr",
        "gf",
        "pf",
        "ga",
        "gm",
        "ge",
        "de",
        "gh",
        "gi",
        "gr",
        "gd",
        "gp",
        "gt",
        "gg",
        "gn",
        "gw",
        "gy",
        "ht",
        "hn",
        "hu",
        "is",
        "in",
        "ir",
        "iq",
        "ie",
        "il",
        "it",
        "jm",
        "jp",
        "jo",
        "kz",
        "kw",
        "kg",
        "lv",
        "lb",
        "ly",
        "li",
        "lt",
        "lu",
        "mk",
        "ml",
        "mt",
        "mq",
        "mr",
        "mx",
        "md",
        "mc",
        "me",
        "ma",
        "nl",
        "nz",
        "ni",
        "ng",
        "no",
        "pk",
        "pa",
        "py",
        "pe",
        "ph",
        "pl",
        "pt",
        "pr",
        "qa",
        "ro",
        "lc",
        "sm",
        "sa",
        "sn",
        "rs",
        "sc",
        "sl",
        "sk",
        "si",
        "so",
        "za",
        "kr",
        "es",
        "sr",
        "se",
        "ch",
        "sy",
        "st",
        "tw",
        "tj",
        "tg",
        "tt",
        "tn",
        "tr",
        "tc",
        "ua",
        "ae",
        "us",
        "uy",
        "uz",
        "ve",
        "ye",
    ]
    """Supported country codes ISO 2 lowercase"""

    region: str
    """
    Region code for more specific geographic targeting. The city parameter can only
    be used when region is also provided.
    """

    type: Literal["anchor_proxy"]
    """
    Create a session with a proxy to access websites as if you're browsing from a
    computer in that country.
    """


class TaskBrowserDefaultConfigurationProxyCustomProxy(TypedDict, total=False):
    active: Required[bool]

    password: Required[str]
    """Proxy password"""

    server: Required[str]
    """
    Proxy address in **PROTOCOL://HOST:PORT** format (e.g.,
    https://proxy.example.com:443). See [proxy page](/advanced/proxy#custom-proxy).
    """

    type: Required[Literal["custom"]]

    username: Required[str]
    """Proxy username"""


TaskBrowserDefaultConfigurationProxy: TypeAlias = Union[
    TaskBrowserDefaultConfigurationProxyAnchorProxy, TaskBrowserDefaultConfigurationProxyCustomProxy
]


class TaskBrowserDefaultConfigurationRecording(TypedDict, total=False):
    """Configuration for session recording."""

    active: bool
    """Enable or disable video recording of the browser session. Defaults to `true`."""


class TaskBrowserDefaultConfigurationTimeout(TypedDict, total=False):
    """Timeout configurations for the browser session."""

    idle_timeout: int
    """
    The amount of time (in minutes) the browser session waits for new connections
    after all others are closed before stopping. Defaults to `5`.
    """

    max_duration: int
    """Maximum amount of time (in minutes) for the browser to run before terminating.

    Defaults to `20`.
    """


class TaskBrowserDefaultConfiguration(TypedDict, total=False):
    """Optional default browser/session configuration when running this task"""

    initial_url: str
    """The URL to navigate to when the browser session starts.

    If not provided, the browser will load an empty page.
    """

    live_view: TaskBrowserDefaultConfigurationLiveView
    """Configuration for live viewing the browser session."""

    proxy: TaskBrowserDefaultConfigurationProxy
    """Proxy Documentation available at [Proxy Documentation](/advanced/proxy)"""

    recording: TaskBrowserDefaultConfigurationRecording
    """Configuration for session recording."""

    timeout: TaskBrowserDefaultConfigurationTimeout
    """Timeout configurations for the browser session."""
