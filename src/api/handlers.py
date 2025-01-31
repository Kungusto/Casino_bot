from aiogram.filters import CommandStart, Command
from aiogram import Router
from aiogram.types import Message

from src.services.casino import Casino

from src.repositories.user import UsersRepository
from src.databases.database import async_session_maker

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message) :
    async with async_session_maker() as session :
        ...
    await message.answer('Добро пожаловать!')
