from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import datetime

from source.schemas.reservation import ReservationCreate, Reservation
from source.schemas.holiday import Holidays
from source.schemas.calendar import CalendarsCreate, Calendars
from source.db import get_db
from source.crud.reservation import create_reservation, fetch_reservations
from source.crud.holiday import fetch_holidays, store_holidays, delete_holidays
from source.crud.calendar import create_calendars_in_db, find_calendars_by_date, fetch_calendars

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

@app.post("/reservations", response_model=Reservation)
async def create_reservation_form(reservation_form: ReservationCreate, db: Session = Depends(get_db)):
  return create_reservation(db, reservation_form)

@app.get("/holidays")
async def get_holidays(start_date: datetime.date | None = None, end_date: datetime.date | None = None, db: Session = Depends(get_db)):
  return fetch_holidays(db, start_date, end_date)

@app.post("/calendars")
async def create_calendars(calendars: CalendarsCreate, db: Session = Depends(get_db)):
  result = create_calendars_in_db(db, calendars)
  return result

@app.get("/calendars", response_model=List[Calendars])
def get_calendars(db: Session = Depends(get_db)):
  result = fetch_calendars(db)
  return result

@app.post("/holidays", response_model=Holidays)
async def create_holidays(holidays: Holidays, db: Session = Depends(get_db)):
  return store_holidays(db, holidays)

@app.delete("/holidays")
async def delete_holidays_controller(holidays: Holidays, db: Session = Depends(get_db)):
  return delete_holidays(db, holidays)