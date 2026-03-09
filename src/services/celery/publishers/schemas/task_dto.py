from pydantic import BaseModel


class TaskResponseDto(BaseModel):
    id: str
    status: str
    queue_name: str
    task_name: str
