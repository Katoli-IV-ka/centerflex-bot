from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.admin_keyboards import admin_keyboard
from keyboards.user_keyboards import start_keyboard

router = Router()


@router.message(Command('start'))
async def cmd_start(msg: types.Message, state: FSMContext):
    # сбрасываем все состояния
    await state.clear()

    # Отправляем приветственное сообщение
    await msg.answer(
        text="Привет! Я бот-каталог товаров. Чтобы узнать список доступных команд, введите /help",
        reply_markup=start_keyboard()
    )


@router.message(Command('admin'))
async def cmd_admin(msg: types.Message, state: FSMContext):
    # сбрасываем все состояния
    await state.clear()

    # Отправляем меню администратора
    await msg.answer(text="Здесь ты можешь упралять ботом", reply_markup=admin_keyboard())


