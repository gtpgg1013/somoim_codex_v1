from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .database import Base, SessionLocal, engine

app = FastAPI(title="Somoim API")

# Create database tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    return {"status": "ok"}
