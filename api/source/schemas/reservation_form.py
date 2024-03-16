import datetime
from pydantic import BaseModel, Field

class ReservationFromBase(BaseModel):
    reservation_date: datetime.date = Field(example="2024-01-01", description="予約日")
    name: str = Field(example="サンプル　太郎", max_length=255, description="名前")
    email_address: str = Field(example="example@example.com", max_length=255, description="メールアドレス")
    phone_number: str = Field(example="090-1234-5678", max_length=255, description="電話番号")

class ReservationFormCreate(ReservationFromBase):
    pass

class ReservationForm(ReservationFromBase):
    id: int