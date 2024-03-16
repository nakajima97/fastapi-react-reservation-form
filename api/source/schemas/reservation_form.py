import datetime
from pydantic import BaseModel, Field

class ReservationForm(BaseModel):
    id: int
    reservation_date: datetime.date
    name: str
    email_address: str
    phone_number: str