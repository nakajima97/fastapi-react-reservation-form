from fastapi import FastAPI

from source.schemas.reservation_form import ReservationFormCreate, ReservationForm

app = FastAPI()

@app.get("/")
async def hello():
  return {"message": "Hello World"}

@app.post("/reservation-form", response_model=ReservationForm)
async def create_reservation_form(reservation_form: ReservationFormCreate):
  return ReservationForm(id=1, **reservation_form.dict())