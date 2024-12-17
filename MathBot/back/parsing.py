from aiogram import Router, F
from aiogram.enums import ContentType

from aiogram.types import Message


parse_router = Router()





@parse_router.message(F.text.regexp('(?i)Задача.+'))
async def parse(message: Message, bot):
    print("Сообщение получено!")
    await bot.send_message(chat_id=1698255704, text=message.text)
    await bot.send_message(chat_id=-4717456332, text=message.text)


@parse_router.message(F.content_type.in_({ContentType.PHOTO,
                                          ContentType.TEXT}))
async def parse_image_text(message: Message, bot):
    print("Сообщение с изображением и текстом получено!")

    text = message.caption if message.caption else "Без текста"

    await bot.send_photo(chat_id=1698255704, photo=message.photo[-1].file_id, caption=text)

    await bot.send_photo(chat_id=-4717456332, photo=message.photo[-1].file_id, caption=text)



