from sqlalchemy import select
from sqlalchemy.orm import Session

import source.models.calendars as calendars_model

def fetch_holidays(db: Session):
    holidays = db.execute(select(calendars_model.Calendars.date).where(calendars_model.Calendars.is_holiday == True)).fetchall()
    return {"holidays": [holiday[0] for holiday in holidays]}