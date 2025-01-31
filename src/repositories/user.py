from src.models.users import UsersOrm
from src.databases.database import Base
from src.schemas.users import Users
from src.repositories.base import BaseRepository

class UsersRepository(BaseRepository) : 
    model = UsersOrm
    schema = Users
    


