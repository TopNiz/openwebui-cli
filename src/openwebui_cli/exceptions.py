"""Public exception hierarchy."""


class OpenWebUIError(RuntimeError):
    """Base error for the high-level client and configuration layer."""


class ConfigurationError(OpenWebUIError):
    """Raised when a profile or credential cannot be resolved safely."""


class APIError(OpenWebUIError):
    """Raised when Open WebUI rejects a request or cannot be reached."""

    def __init__(self, message: str, *, status_code: int | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code


class ValidationError(OpenWebUIError):
    """Raised before sending an invalid or unsafe mutation."""
