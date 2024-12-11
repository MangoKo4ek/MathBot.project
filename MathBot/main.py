from back.parsing import parse_router
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from front.register import register_router
import asyncio
import logging
from back.db import init_db

# Настройка логирования
logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
    level=logging.INFO
)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Создание роутера


# Включение роутера в диспетчер
dp.include_router(register_router)
dp.include_router(parse_router)


# Основная функция запуска бота
async def main():
    await init_db()
    await dp.start_polling(bot)


# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
