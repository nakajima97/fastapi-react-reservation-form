from pydantic import BaseModel, Field

class CalendarsBase(BaseModel):
  date: str = Field(example="2024-01-01", description="日付")

class CalendarsCreate(CalendarsBase):
  pass

class Calendars(CalendarsBase):
  id: int

  class Config:
    from_attributes = True