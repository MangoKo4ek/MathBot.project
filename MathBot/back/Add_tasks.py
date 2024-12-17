from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import back.db as db
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

task_router = Router()


class Task(StatesGroup):
    text = State()
    points = State()


@task_router.message(Command("add_task"))
async def add_task(message: Message, state: FSMContext):
    await message.answer('введите текст задачи')
    await state.set_state(Task.text)


@task_router.message(Task.text)
async def task_text(message: Message, state: FSMContext):

    await db.add_task(message.text)
    await message.answer('текст добавлен')
    await state.clear()
