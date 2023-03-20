from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancelLoadPhotoKb = InlineKeyboardMarkup().row(
    InlineKeyboardButton(text="Отменить загрузку фотографий", callback_data="cancel_load_photo"),
    InlineKeyboardButton(text="Вернуться в меню", callback_data="to_catalog_menu")
)
