from aiogram.filters import CommandStart, Command
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.services.casino import Casino, CasinoFactory
from src.schemas.users import UsersSetBalance
from src.repositories.user import UsersRepository
from src.databases.database import async_session_maker

class Input(StatesGroup) :
    password = State()
    new_password = State()
    set_balance = State()

router = Router()

# id|tg_id|balance|password|registrated|last_game|
# --+-----+-------+--------+-----------+---------+

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) :
    async with async_session_maker() as session :
        is_new = await Casino.new_user(int(message.from_user.id))
        if is_new :
            message.answer('Добро пожаловать в моего бота) придумай-ка пароль')
            await state.set_state(Input.new_password)
        else :
            await message.answer('Выберите игру')    
    
    
@router.message(Input.new_password)
async def login_with_pasword(message: Message, state: FSMContext) :
    await message.answer('аощуцшйоуащ')
    async with async_session_maker() as session : 
        await UsersRepository(session).add(tg_id=message.from_user.id, balance=0, password=message.text)
        await session.commit()

@router.message(Command('balance'))
async def edit_balance(message: Message, state: FSMContext) :
    await message.answer('Введите сумму на которую хотите пополнить')
    await state.set_state(Input.set_balance)
    
@router.message(Input.set_balance) 
async def pay_balance(message: Message, state: FSMContext) :
    await state.clear()
    async with async_session_maker() as session : 
        balance = await UsersRepository(session).get_one_or_none(tg_id=message.from_user.id)
        delta_balance = int(message.text)+balance.balance
        await UsersRepository(session).edit(UsersSetBalance(balance=delta_balance), tg_id=message.from_user.id, is_patch=True)
        await session.commit()
        
