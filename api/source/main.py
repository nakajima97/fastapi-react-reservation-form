from fastapi import FastAPI

from source.schemas.reservation import ReservationCreate, Reservation

app = FastAPI()

@app.post("/reservation", response_model=Reservation)
async def create_reservation_form(reservation_form: ReservationCreate):
  return Reservation(id=1, **reservation_form.dict())