from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


# future: rename to admin_menu
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


def cancel_keyboard(data='', skip_to: str = False) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Отменить добавление товара', callback_data='cancel_add_product-'+data)
    if skip_to:
        keyboard.button(text='Пропустить', callback_data=skip_to)
    return keyboard.as_markup()


def save_product_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Название', callback_data='edit_title')
    keyboard.button(text='Фото', callback_data='edit_photo')
    keyboard.button(text='Описание', callback_data='edit_description')
    keyboard.button(text='Цена', callback_data='edit_description')
    keyboard.button(text='Скрыть', callback_data='hide_product')
    keyboard.button(text='Удалить', callback_data='remove_product')
    keyboard.adjust(2, 2, 1, 1)
    return keyboard.as_markup()


