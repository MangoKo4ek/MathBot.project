from aiogram import Router, F

from aiogram.types import Message

from config import ADMIN_ID, GROUP_ID

parse_router = Router()


@parse_router.message(F.text.regexp('(?i)Задача.+'))
async def parse(message: Message, bot):
    print("Сообщение получено!")
    await bot.send_message(chat_id=ADMIN_ID, text=message.text)
    await bot.send_message(chat_id=GROUP_ID, text=message.text)
