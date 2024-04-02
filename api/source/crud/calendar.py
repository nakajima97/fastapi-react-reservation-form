from sqlalchemy.orm import Session

import source.models.calendars as calendars_model
import source.schemas.calendar as calendar_schema

def create_calendars_in_db(db: Session, calendars: calendar_schema.CalendarsCreate):
    insert_calendar = calendars_model.Calendars(**calendars.dict());
    db.add(insert_calendar);
    db.commit()
    db.refresh(insert_calendar)
    return {"calendars": insert_calendar}
