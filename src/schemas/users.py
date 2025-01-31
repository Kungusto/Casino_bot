from pydantic import BaseModel, Field

from datetime import datetime 

class Users(BaseModel) : 
    id : int
    tg_id: str
    balance: int
    registrated: datetime
    password: str
    