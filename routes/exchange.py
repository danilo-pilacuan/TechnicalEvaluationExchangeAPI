from typing import List
from fastapi import Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from models.exchange import Exchanges
from schemas.exchange import Exchange
import requests


from config.db import SessionLocal, engine
import models.exchange

models.exchange.Base.metadata.create_all(bind=engine)
exchangeRouter = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@exchangeRouter.get("/", response_model=List[Exchange])
def getRates(db: Session = Depends(get_db)):
    result = db.query(Exchanges).all()
    r = requests.post('https://webhook.site/aab6cb55-0073-4982-aaf3-6f153d4c61dd', json=jsonable_encoder(result))
    return result