from sqlalchemy.orm import Session
from sqlalchemy import select

import source.models.calendars as calendars_model
import source.schemas.calendar as calendar_schema

def create_calendars_in_db(db: Session, calendars: calendar_schema.CalendarsCreate):
    for date in calendars.dates:
        if(db.query(calendars_model.Calendars).filter(calendars_model.Calendars.date == date).first()):
            continue
        db_calendar = calendars_model.Calendars(date=date, is_holiday=False)
        db.add(db_calendar)
    db.commit()
    return {"message": "Calendars created successfully."}

def find_calendars_by_date(db: Session, date: str):
    return db.query(calendars_model.Calendars).filter(calendars_model.Calendars.date == date).first()

def fetch_calendars(db: Session):
    result = db.execute(select(calendars_model.Calendars.id, calendars_model.Calendars.date, calendars_model.Calendars.is_holiday))
    return result.all()