from src.databases.database import Base

from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import mapped_column, Mapped

from datetime import datetime 

class UsersOrm(Base) : 
    __tablename__ = 'casino_users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[str]
    balance: Mapped[int] 
    registrated: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    last_game: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    password: Mapped[str] = mapped_column(String(30))
    
    
    