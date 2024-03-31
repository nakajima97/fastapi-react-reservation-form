from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from source.schemas.reservation import ReservationCreate, Reservation
from source.schemas.holiday import Holidays
from source.schemas.calendar import Calendars
from source.db import get_db
from source.crud.reservation import create_reservation, fetch_reservations
from source.crud.holiday import fetch_holidays

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

@app.get("/reservations", response_model=list[Reservation])
async def get_reservation(db: Session = Depends(get_db)):
  return fetch_reservations(db)

@app.post("/reservation", response_model=Reservation)
async def create_reservation_form(reservation_form: ReservationCreate, db: Session = Depends(get_db)):
  return create_reservation(db, reservation_form)

@app.get("/holidays", response_model=Holidays)
async def get_holidays(db: Session = Depends(get_db)):
  return fetch_holidays(db)

@app.post("/calendars", response_model=Calendars)
async def create_calendars():
  return {"calendars": ["2024-01-01", "2024-01-02"]}