from pydantic import BaseModel
from typing import Optional, Dict


class TaskInput(BaseModel):
    title: str
    description: str
    deadline: str
    importance: int
    effort: int


class PrioritizedTask(TaskInput):
    score: float
    breakdown: Dict[str, float]
    reason: Optional[str] = None
