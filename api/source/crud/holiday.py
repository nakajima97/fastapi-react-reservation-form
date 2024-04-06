from sqlalchemy import select
from sqlalchemy.orm import Session

import datetime

import source.models.calendars as calendars_model
import source.schemas.holiday as holiday_schema

def fetch_holidays(db: Session, start_date: datetime.date | None = None, end_date: datetime.date | None = None):
    # holidays = db.execute(select(calendars_model.Calendars.date).where(calendars_model.Calendars.is_holiday == True)).fetchall()
    # return {"holidays": [holiday[0] for holiday in holidays]}
    query = db.query(calendars_model.Calendars.date).filter(calendars_model.Calendars.is_holiday == True)
    if start_date:
        query = query.filter(calendars_model.Calendars.date >= start_date)
    if end_date:
        query = query.filter(calendars_model.Calendars.date <= end_date)
    result = query.all()
    return {"holidays": [holiday[0] for holiday in result]}

def store_holidays(db: Session, holidays: holiday_schema.Holidays):
    for holiday in holidays.holidays:
        calendar = db.query(calendars_model.Calendars).filter(calendars_model.Calendars.date == holiday).first()
        if not calendar:
            continue
        calendar.is_holiday = True
    db.commit()
    return holidays

def delete_holidays(db: Session, holidays: holiday_schema.Holidays):
    for holiday in holidays.holidays:
        calendar = db.query(calendars_model.Calendars).filter(calendars_model.Calendars.date == holiday).first()
        if not calendar:
            continue
        calendar.is_holiday = False
    db.commit()
    return holidays