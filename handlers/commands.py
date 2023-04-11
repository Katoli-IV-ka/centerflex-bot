from aiogram import types, Router
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    # Отправляем приветственное сообщение
    await message.answer("Привет! Я бот-каталог товаров. Чтобы узнать список доступных команд, введите /help")
