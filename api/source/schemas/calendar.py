from pydantic import BaseModel, Field
from typing import List
import datetime

class CalendarsBase(BaseModel):
  date: datetime.date = Field(example="2024-01-01", description="日付")

class CalendarsCreate(BaseModel):
  dates: List[datetime.date] = Field(example=["2024-01-01", "2024-01-02"], description="日付")

class Calendars(CalendarsBase):
  id: int
  is_holiday: bool = Field(example=False, description="祝日かどうか")

  class Config:
    from_attributes = True

class CalendarsList(BaseModel):
  items: List[Calendars]