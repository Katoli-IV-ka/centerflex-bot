from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


catalogMenuKb = ReplyKeyboardMarkup(
    resize_keyboard=True,
).row(
    KeyboardButton(text='Добавить товар'),
    KeyboardButton(text='Пос в меню')
).row(
    KeyboardButton(text='Назад в меню')
)


loadPhotoKb = ReplyKeyboardMarkup().row(
    KeyboardButton(text="Cохранить фото", callback_data="add_photo_to_catalog"),
    KeyboardButton(text="Назад/Отменить загруку", callback_data="back_to_add_tittle")
)




