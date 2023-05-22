from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def notification_control_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='добавить в очередь', callback_data='add_to_queue')
    keyboard.button(text='изменить очередь', callback_data='edit_to_queue')
    return keyboard.as_markup()

