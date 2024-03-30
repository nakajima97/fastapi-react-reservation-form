from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from source.schemas.reservation import ReservationCreate, Reservation
from source.schemas.holiday import Holidays
from source.db import get_db
from source.crud.reservation import create_reservation

app = FastAPI()

origins = [
  'http://localhost:5173',
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.post("/reservation", response_model=Reservation)
async def create_reservation_form(reservation_form: ReservationCreate, db: Session = Depends(get_db)):
  return create_reservation(db, reservation_form)

@app.get("/holidays", response_model=Holidays)
async def get_holidays():
  return Holidays(holidays=["2024-01-01", "2024-01-02"])