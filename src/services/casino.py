import random
from datetime import datetime 

from src.schemas.users import Users

from src.databases.database import async_session_maker
from src.repositories.user import UsersRepository

# id|tg_id|balance|password|registrated|last_game|
# --+-----+-------+--------+-----------+---------+

class Casino :
    current_sessions = {}
    casino_balance = 1000000
    
    
    def __init__(self, tg_id,  balance, base_chance, jackpot_chance, temp_bet=0, last_game=datetime.now()) :
        self.__tg_id = tg_id
        self.__balance = balance
        self.__base_chance = base_chance
        self.__jackpot_chance = jackpot_chance
        self.__temp_bet = temp_bet
        self.__last_game = last_game
    
    def __dict__(self) :
        return {
            'tg_id' : self.tg_id, 
            'balance' : self.balance,
            'last_game' : self.last_game
        }

    @staticmethod
    async def new_user(tg_id) :
        async with async_session_maker() as session :
            model = await UsersRepository(session).get_one_or_none(tg_id=tg_id)
        
        if model is None :
            return True
        
        return False

    def randomize(self) :
        if random.random() > self.base_chance :
            return True 
        else : 
            return False
        
    def game(self) :
        ...
        
    async def save(self) :
        async with async_session_maker() as session:
            if UsersRepository(session).get_one_or_none(tg_id=self.tg_id) :
                UsersRepository(session).edit(self.__dict__) 
        
    @property
    def balance(self): 
        return self.__balance
    
    @balance.setter
    def balance(self, value): 
        self.__balance = value

    @property
    def last_game(self): 
        return self.__last_game
    
    @last_game.setter
    def balance(self, value): 
        self.last_game = value
        
    @property
    def base_chance(self) :
        return self.__base_chance
    
    @base_chance.setter
    def base_chance(self, value) :
        self.__base_chance = value
    
    @property
    def jackpot_chance(self) :
        return self.__jackpot_chance
    
    @jackpot_chance.setter
    def base_chance(self, value) :
        self.jackpot_chance = value
    
    @property
    def temp_bet(self) :
        return self.__temp_bet
    
    @temp_bet.setter
    def base_chance(self, value) :
        self.__temp_bet = value

    @property
    def tg_id(self) :
        return self.__temp_bet
        
        
class CasinoFactory : 
    @staticmethod
    def create_base_user(self, tg_id, balance=0, base_chance=0.45, jackpot_chance=0.01) : 
        player = Casino(self, balance, base_chance, jackpot_chance, temp_bet=0)
        return player
    
    @staticmethod
    async def get_user_data(self, tg_id) -> Users: 
        async with async_session_maker() as session : 
            result = await UsersRepository(session).get_one_or_none(tg_id=tg_id)
            return result
            
