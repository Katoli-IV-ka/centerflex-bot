from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def getSaveKb(callback_data) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Сохранить', callback_data=f'{callback_data}')
    return keyboard.as_markup()
