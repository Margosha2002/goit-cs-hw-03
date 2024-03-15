from typing import Optional
from sqlmodel import Field, SQLModel


class Task(SQLModel, table=True):
    __tablename__ = "tasks"
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    status_id: int = Field(foreign_key="status.id")
    user_id: int = Field(foreign_key="users.id")
