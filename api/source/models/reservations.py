from sqlalchemy import Column, String, DateTime, Integer, Date

from source.db import Base

class Reservations(Base):
  __tablename__ = "reservations"

  id = Column(Integer, primary_key=True, index=True)
  reservation_date = Column(Date)
  name = Column(String(255))
  email_address = Column(String(255))
  phone_number = Column(String(255))
  created_at = Column(DateTime)