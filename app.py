from fastapi import Depends, FastAPI, HTTPException
from routes.exchange import exchangeRouter

app=FastAPI()
app.include_router(exchangeRouter)