from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboardAddOptional = InlineKeyboardMarkup().row(
    InlineKeyboardButton(text="📌 Заголовок", callback_data="edit_tittle"),
    InlineKeyboardButton(text="📷 Фотографии", callback_data="edit_photo")
).row(
    InlineKeyboardButton(text="💰 Цена", callback_data="edit_price"),
    InlineKeyboardButton(text="📄 Описание", callback_data="edit_caption"),
).row(
    InlineKeyboardButton(text="🐵 Показать в каталоге", callback_data="view_in_catalog") # скрыть из каталога
)

# InlineKeyboardButton(text="🙈 Скрыть из каталога", callback_data="hide_in_catalog")
