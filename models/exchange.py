from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import INTEGER, VARCHAR, DATE, REAL
from config.db import Base

class Exchanges(Base):
    __tablename__ = "exchangeRates"
    id=Column("id", INTEGER, primary_key=True, autoincrement=True, index=True, nullable=False)
    exchangeDate=Column(DATE,nullable=True)
    open=Column(REAL)
    high=Column(REAL)
    low=Column(REAL)
    close=Column(REAL)
    adjClose=Column(REAL)
