import datetime
from pydantic import BaseModel, Field

class Holidays(BaseModel):
    holidays: list[datetime.date] = Field(example=["2024-01-01", "2024-01-02"], description="休日")