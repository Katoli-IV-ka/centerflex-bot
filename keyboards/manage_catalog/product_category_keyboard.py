from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database import get_data


async def product_category_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    categories = await get_data(table_name='categories')

    for c in categories:
        keyboard.button(text=c[1], callback_data=f'enter_category_{c[0]}')

    add_category_button = InlineKeyboardButton(text='Добавить категорию', callback_data='catalog_add_category')
    keyboard.row(add_category_button, width=1)

    return keyboard.as_markup()
