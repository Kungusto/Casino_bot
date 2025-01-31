# юз: @Lucky_Star_Casino_bot

import asyncio
from aiogram import Dispatcher, Bot
import logging

from src.api.handlers import router
from config import settings

bot = Bot(token=settings.TOKEN) 
dp = Dispatcher()

async def main() :
    await dp.start_polling(bot)
    
if __name__ == '__main__' :
    dp.include_router(router)
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
    
