from typing import Optional
from pydantic import BaseModel

class Course(BaseModel):
    id: Optional[int] = None
    titulo: str
    lessons: int
    hours: int