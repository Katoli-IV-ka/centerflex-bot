from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Каталог товаров', callback_data='catalog')
    keyboard.button(text='Быстрый запрос', callback_data='fast_request')
    keyboard.button(text='О нас', callback_data='about')
    keyboard.adjust(1, 2)
    return keyboard.as_markup()
