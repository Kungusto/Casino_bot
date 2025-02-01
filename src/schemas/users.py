from pydantic import BaseModel, Field

from datetime import datetime 

class Users(BaseModel) : 
    id : int
    tg_id: int
    balance: int
    registrated: datetime = datetime.now()
    last_game: datetime = datetime.now()

class UsersSetBalance(BaseModel) :
    balance: int