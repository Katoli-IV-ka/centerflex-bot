from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def getBackToKb(text='В меню', callback='adm_to_menu', cancel_button=False) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=f'{text}', callback_data=f'{callback}')
    if cancel_button:
        keyboard.button(text='В меню', callback_data='adm_to_menu')
    keyboard.adjust(2)
    return keyboard.as_markup()
