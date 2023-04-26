from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def admin_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Изменять каталог', callback_data='edit_catalog')
    keyboard.button(text='Добавить в каталог', callback_data='catalog_admin')
    keyboard.button(text='Очередь уведомлений', callback_data='notification_queue')
    keyboard.button(text='Изменить информацию', callback_data='edit_info')
    keyboard.adjust(2, 1, 1)
    return keyboard.as_markup()





