from pydantic import BaseModel


class DetailError(BaseModel):
    step: str
    exception: str
