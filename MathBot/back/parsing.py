from aiogram import Router, F

from aiogram.types import Message

from config import ADMIN_ID, GROUP_ID

parse_router = Router()


@parse_router.message(F.text.regexp('(?i)Задача.+'))
async def parse(message: Message, bot):
    print("Сообщение получено!")
    await bot.send_message(chat_id=ADMIN_ID, text=message.text)
    await bot.send_message(chat_id=GROUP_ID, text=message.text)


@parse_router.message(F.photo & F.text.regexp('(?i)Задача.+'))
async def parse_image_text(message: Message, bot):
    print("Сообщение с изображением и текстом получено!")
    
    text = message.caption if message.caption else "Без текста"
    
    await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=text)
 
    await bot.send_photo(chat_id=GROUP_ID, photo=message.photo[-1].file_id, caption=text)
