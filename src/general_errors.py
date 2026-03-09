from typing import Optional

from src.schemas.errors_dto import DetailError


class ServiceError(Exception):
    def __init__(
        self, message: str = "Erro interno", cause: Optional[Exception] = None
    ):
        super().__init__(message)
        self.cause = cause


class ModelValidationError(ServiceError):
    def __init__(
        self,
        message: str,
        cause: Optional[Exception] = None,
        details: Optional[DetailError] = None,
    ):
        super().__init__(message, cause)
        self.details = details.model_dump(mode="json") if details is not None else {}


class FilterValidationError(ServiceError):
    def __init__(
        self,
        message: str,
        cause: Optional[Exception] = None,
        details: Optional[DetailError] = None,
    ):
        super().__init__(message, cause)
        self.details = details.model_dump(mode="json") if details is not None else {}


class HttpServiceError(ServiceError):
    def __init__(
        self,
        message: str,
        cause: Optional[Exception] = None,
        details: Optional[DetailError] = None,
    ):
        super().__init__(message, cause)
        self.details = details.model_dump(mode="json") if details is not None else {}


class PageExecutionError(ServiceError):
    def __init__(
        self,
        message: str,
        cause: Optional[Exception] = None,
        details: Optional[DetailError] = None,
    ):
        super().__init__(message, cause)
        self.details = details.model_dump(mode="json") if details is not None else {}


class DatabaseConnectionError(ServiceError):
    def __init__(
        self,
        message: str,
        cause: Optional[Exception] = None,
        details: Optional[DetailError] = None,
    ):
        super().__init__(message, cause)
        self.details = details.model_dump(mode="json") if details is not None else {}
        self.details = details.model_dump(mode="json") if details is not None else {}
