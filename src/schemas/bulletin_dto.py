from datetime import date
from typing import Optional, Union

from pydantic import BaseModel, Field, field_validator

from src.schemas.domains import PeriodType, PipelineType
from src.schemas.worker_dto import WorkerStatus


class BulletinRequestDto(BaseModel):
    period: PeriodType = Field(default=PeriodType.MRN)
    target_date: Union[date, str]
    type: Optional[PipelineType] = Field(default=PipelineType.BULLETING)

    @field_validator("target_date", mode="before")
    @classmethod
    def parse_date(cls, v) -> Union[date, str]:
        if isinstance(v, date):
            return v

        if isinstance(v, str) and len(v) == 10:
            try:
                if (v[4] == "-" or v[4] == "/") and (v[7] == "-" or v[7] == "/"):
                    y, m, d = v.split("/") if v.__contains__("/") else v.split("-")
                    return date(int(y), int(m), int(d))
                else:
                    d, m, y = v.split("/") if v.__contains__("/") else v.split("-")
                    return date(int(y), int(m), int(d))
            except Exception:
                raise ValueError("Date must be valid")
        raise ValueError(f"Date must be valid {v}")


class BulletinResponseDto(BaseModel):
    id: str
    status: WorkerStatus
    queue_name: str
    task_name: str
