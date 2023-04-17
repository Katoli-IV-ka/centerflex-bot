from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


# future: rename to admin menu
def admin_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Изменять каталог', callback_data='edit_catalog')
    keyboard.button(text='Добавить в каталог', callback_data='add_product')
    keyboard.button(text='Очередь уведомлений', callback_data='notification_queue')
    keyboard.button(text='Изменить информацию', callback_data='edit_info')
    keyboard.adjust(2, 1, 1)
    return keyboard.as_markup()


def go_to_keyboard(callback_data, text='Далее') -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=text, callback_data=callback_data)
    return keyboard.as_markup()


def cancel_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Отменить добавление товара', callback_data='cancel_add_product')
    return keyboard.as_markup()


# Похоже что клавиатуры ниже будут заменены билдером go_to_keyboard
def to_admin_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='В меню', callback_data='add_product')
    return keyboard.as_markup()


def to_photo_keyboard(text='Далее') -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=text, callback_data='to_photo')
    return keyboard.as_markup()


def to_title_keyboard(text='Далее') -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=text, callback_data='to_photo')
    return keyboard.as_markup()


def to_description_keyboard(text='Далее') -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=text, callback_data='to_description')
    return keyboard.as_markup()


def to_price_keyboard(text='Далее') -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=text, callback_data='to_price')
    return keyboard.as_markup()
