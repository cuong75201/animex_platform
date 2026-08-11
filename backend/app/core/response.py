from typing import Any, Generic, Optional, TypeVar

from fastapi_responseschema import AbstractResponseSchema
from pydantic import BaseModel


class ResponseMetadata(BaseModel):
    error:bool
    message: str | None

T= TypeVar("T")

class ResponseSchema(AbstractResponseSchema[T],Generic[T]):
    data:T
    meta:ResponseMetadata

    @classmethod
    def from_exception(cls, reason, status_code, message: str = "Error", **others):
        return cls(
            data=reason,
            meta=ResponseMetadata(error=status_code >= 400, message=message)
        )

    @classmethod
    def from_api_route(
        cls, content: Any, status_code: int, description: Optional[str] = None, **others
    ):
        return cls(
            data=content,
            meta=ResponseMetadata(error=status_code >= 400, message=description)
        )

