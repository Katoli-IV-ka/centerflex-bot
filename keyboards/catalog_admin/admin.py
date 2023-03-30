from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def getCatalogAdminKb() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Добавить товар в каталог', callback_data='add_item')
    keyboard.button(text='future:Категории', callback_data='future')
    keyboard.button(text='future:Админы', callback_data='future')
    keyboard.adjust(1, 2)
    return keyboard.as_markup()

