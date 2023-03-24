

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboardGo = InlineKeyboardMarkup().row(
    InlineKeyboardButton(text='Go', callback_data='go')
)

