import datetime
from pydantic import BaseModel, Field
from typing import Union

class Holidays(BaseModel):
    holidays: list[datetime.date] = Field(default_factory=list, example=["2024-01-01", "2024-01-02"], description="休日")