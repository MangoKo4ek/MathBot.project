from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message
import back.db as db


class User(StatesGroup):
    first_name = State()


register_router = Router()


@register_router.message(Command('start'))
async def signup(message: Message, state: FSMContext):
    if await db.user_exists(message.from_user.id):
        await message.answer('пользователь уже был создан')
    else:
        await message.answer('введите своё имя')
        await state.set_state(User.first_name)


@register_router.message(User.first_name)
async def signup(message: Message, state: FSMContext):
    await db.create_user(message.from_user.id, message.text)
    await message.answer('пользователь создан')
    await state.clear()
