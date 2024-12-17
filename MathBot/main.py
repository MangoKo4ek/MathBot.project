from back.parsing import parse_router
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from front.register import register_router
import asyncio
import logging
from back.db import init_db

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
    level=logging.INFO
)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(register_router)
dp.include_router(parse_router)


async def main():
    await init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
