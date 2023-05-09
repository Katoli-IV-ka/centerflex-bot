from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def go_to_keyboard(callback_data, text='Далее') -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=text, callback_data=callback_data)
    return keyboard.as_markup()


def cancel_keyboard(skip_to: str = False) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Отменить добавление товара', callback_data='cancel_add_product')
    if skip_to:
        keyboard.button(text='Пропустить', callback_data=skip_to)
    return keyboard.as_markup()


def save_product_keyboard(show_in_catalog: bool = False) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Название', callback_data='edit_title')
    keyboard.button(text='Фото', callback_data='edit_photo')
    keyboard.button(text='Описание', callback_data='edit_description')
    keyboard.button(text='Цена', callback_data='show_in_catalog')
    if not show_in_catalog:
        keyboard.button(text='Скрыть', callback_data='hide_in_catalog')
    else:
        keyboard.button(text='Опубликовать', callback_data='show_in_catalog')
    keyboard.button(text='Удалить', callback_data='remove_product')
    keyboard.adjust(2, 2, 1, 1)
    return keyboard.as_markup()
