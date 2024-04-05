from sqlalchemy import select
from sqlalchemy.orm import Session

import source.models.calendars as calendars_model
import source.schemas.holiday as holiday_schema

def fetch_holidays(db: Session):
    holidays = db.execute(select(calendars_model.Calendars.date).where(calendars_model.Calendars.is_holiday == True)).fetchall()
    return {"holidays": [holiday[0] for holiday in holidays]}

def store_holidays(db: Session, holidays: holiday_schema.Holidays):
    for holiday in holidays.holidays:
        calendar = db.query(calendars_model.Calendars).filter(calendars_model.Calendars.date == holiday).first()
        if not calendar:
            continue
        calendar.is_holiday = True
    db.commit()
    return holidays