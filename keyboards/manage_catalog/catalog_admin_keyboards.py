from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def next_step_keyboard(callback_data, text='Далее') -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=text, callback_data=callback_data)
    return keyboard.as_markup()


def cancel_keyboard(back_to='cancel_add_product', skip_to: str = False) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Вернуться в меню', callback_data=back_to)
    if skip_to:
        keyboard.button(text='Пропустить', callback_data=skip_to)
    return keyboard.as_markup()


def save_product_keyboard(show_in_catalog: bool = False) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Название', callback_data='change_title')
    keyboard.button(text='Фото', callback_data='change_photo')
    keyboard.button(text='Описание', callback_data='change_description')
    keyboard.button(text='Цена', callback_data='change_price')
    if not show_in_catalog:
        keyboard.button(text='Скрыть', callback_data='change_display_hide')
    else:
        keyboard.button(text='Опубликовать', callback_data='change_display_show')
    keyboard.button(text='Удалить', callback_data='remove_product')
    keyboard.adjust(2, 2, 1, 1)
    return keyboard.as_markup()
