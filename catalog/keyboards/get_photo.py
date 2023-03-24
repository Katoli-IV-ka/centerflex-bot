from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboardSavePhoto = ReplyKeyboardMarkup(
    resize_keyboard=True,
).row(
    KeyboardButton(text="Cохранить фото")
).row(
    KeyboardButton(text="Назад к названию"),
    KeyboardButton(text="Не добавлять товар")
)
