from pydantic import BaseModel, Field

class Calendars(BaseModel):
  calendars: list[str] = Field(example=["2024-01-01", "2024-01-02"], description="カレンダー")