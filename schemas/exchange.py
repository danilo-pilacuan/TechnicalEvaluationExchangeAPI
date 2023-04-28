from datetime import date
from typing import Optional
from pydantic import BaseModel

class Exchange(BaseModel):
    id:Optional[int]
    exchangeDate:date
    open:float
    high:float
    low:float
    close:float
    adjClose:float
    class Config:
        orm_mode = True