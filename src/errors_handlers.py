from typing import cast

from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse



# Exception class
class BusinessException(Exception):
    def __init__(
        self, message: str, status_code: int = 400, error_code: str = "BUSINESS_ERROR"
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        super().__init__(message)


class ErrorsHandlers:
    @staticmethod
    async def http(request: Request, exc: Exception) -> JSONResponse:
        exc = cast(HTTPException, exc)
        # Http request
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "code": "HTTP_ERROR",
                    "message": exc.detail,
                },
            },
        )

    @staticmethod
    async def business(request: Request, exc: Exception) -> JSONResponse:
        exc = cast(BusinessException, exc)
        # Bad request
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "code": "BUSINESS_ERROR",
                    "message": exc.message,
                },
            },
        )

    @staticmethod
    async def generic(request: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "code": "INTERNAL_SERVER_ERROR",
                    "message": "Ocorreu um erro interno no servidor.",
                },
            },
        )
