from fastapi import FastAPI

from source.schemas.reservation_form import ReservationForm

app = FastAPI()

@app.get("/")
async def hello():
  return {"message": "Hello World"}

@app.post("/reservation-form")
async def create_reservation_form(reservation_form: ReservationForm):
  return reservation_form