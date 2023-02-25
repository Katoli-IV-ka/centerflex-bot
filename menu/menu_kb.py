from main import bot, dp

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, Message

mainMenuKb = ReplyKeyboardMarkup(
    resize_keyboard=True,
).row(
    KeyboardButton(text='Оставить заявку'),
    KeyboardButton(text='Каталог товаров')
).row(
    KeyboardButton(text='О нас'),
    KeyboardButton(text='Ещё что-то')
)


@dp.message_handler(text="Оставить заявку")
async def application(message: Message):

    # здесь должно изменяться состояние
    await bot.send_message(
        chat_id=message.from_user.id,
        text='''Оставьте вашу заявку, укажите товар и количесво 
------------
Пример:
Финишная шпаклёвка SEMIN AIRLESS, 2 ведра 25 литров'''
    )


@dp.message_handler(text="О нас")
async def application(message: Message):

    # здесь должно изменяться состояние
    await bot.send_message(
        chat_id=message.from_user.id,
        disable_web_page_preview=True,
        text='''Мы являемся прямыми поставщиками и официальными партнёрами Американской компании STRAIT-FLEX , в лице компании CENTER-FLEX , уже много лет занимающейся производством защитных углоформирующих лент из особого запатентованного материала и инструмента для их монтажа.

Покупая ленты и инструмент STRAIT-FLEX у нас , вы получаете полный пакет необходимых документов , всю необходимую информацию об продукте , и самое главное ЛУЧШИЕ ЦЕНЫ
   
Наш адресс: ул. Красногвардейская 150/1 офис 20
Наш сайт: https://centerflex.by/
Email: сenterflex@mail.ru
Телефоны для связи: 
+375(29)204-02-54 
+375(33)672-82-47
'''

    )
