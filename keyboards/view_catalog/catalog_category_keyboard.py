from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database import get_data


async def categories_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    categories = await get_data(table_name='categories')

    for c in categories:
        keyboard.button(text=c[1], callback_data=f'catalog_category_{c[0]}')

    keyboard.adjust(3, repeat=True)

    add_category_button = InlineKeyboardButton(text='Назад', callback_data='-')
    keyboard.row(add_category_button, width=1)

    return keyboard.as_markup()


async def pages_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text=f'В главное меню', callback_data="to_user_menu")
    keyboard.button(text=f'Дальше ', callback_data=f'next_pages')

    return keyboard.as_markup()