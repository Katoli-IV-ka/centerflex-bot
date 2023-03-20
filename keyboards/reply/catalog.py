from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


catalogMenuKb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    #input_field_placeholder='Каталог товаров',
    #is_persistent=True,
    #selective=True,
).row(
    KeyboardButton(text='Добавить товар'),
    KeyboardButton(text='Пос в меню')
).row(
    KeyboardButton(text='Назад в меню')
)


loadPhotoKb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    #one_time_keyboard=False,
).row(
    KeyboardButton(text="Cохранить фото"),
    KeyboardButton(text="Отменить загруку")
)




