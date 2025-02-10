from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from sqlalchemy import Column, Integer, String

router = APIRouter()

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    team = Column(String, index=True)
    goals = Column(Integer, default=0)
    assists = Column(Integer, default=0)
    sport = Column(String, index=True)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/players/")
def get_players(db: Session = Depends(get_db)):
    return db.query(Player).all()
