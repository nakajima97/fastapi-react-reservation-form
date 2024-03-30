from sqlalchemy import Column, Boolean, Date, Integer, DateTime
from datetime import datetime

from source.db import Base

class Calendars(Base):
  __tablename__ = "calendars"

  id = Column(Integer, primary_key=True)
  date = Column(Date, unique=True)
  is_holiday = Column(Boolean, nullable=False, default=False)
  created_at = Column(DateTime, nullable=False, default=datetime.now())
  updated_at = Column(DateTime, nullable=False,default=datetime.now())