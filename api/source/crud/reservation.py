from sqlalchemy.orm import Session
from source.schemas.reservation import ReservationCreate
from source.models.reservations import Reservations

def fetch_reservations(db: Session):
  return db.query(Reservations).all()

def create_reservation(db: Session, reservation_create: ReservationCreate):
  db_reservation = Reservations(**reservation_create.dict())
  db.add(db_reservation)
  db.commit()
  db.refresh(db_reservation)
  return db_reservation