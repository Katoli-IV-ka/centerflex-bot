from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def getOptionsKb(visibility) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Название', callback_data='adm_item_name')
    keyboard.button(text='Фото', callback_data='adm_item_photo')
    keyboard.button(text='Описание', callback_data='adm_item_caption')
    keyboard.button(text='Цена', callback_data='adm_item_price')
    if visibility:
        keyboard.button(text='Скрыть в каталоге', callback_data='adm_item_hide')
    else:
        keyboard.button(text='Показать в каталоге', callback_data='adm_item_show')
    keyboard.adjust(2, 2, 1)
    return keyboard.as_markup()
