from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboardToMenu = InlineKeyboardMarkup().row(
    InlineKeyboardButton(text="Отменить добавлени товара", callback_data="to_menu")
)

