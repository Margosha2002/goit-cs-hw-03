from typing import Optional
from sqlmodel import Field, SQLModel


class Status(SQLModel, table=True):
    __tablename__ = "status"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
