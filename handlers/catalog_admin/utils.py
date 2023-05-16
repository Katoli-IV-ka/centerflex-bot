from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message


def format_product_text(data: dict):
    text = f"*{data['product_title']}*"

    if data['product_description']:
        text += f"\n\n_{data['product_description']}_"

    if data['product_price']:
        text += f"\n\nОриентировочная цена: *{data['product_price']}* руб\."

    text += '\n\n\n🛠` Данное сообщение - это представление того как товар отобразиться в каталоге\ (без этой подписи). `'
    text += '`Чтобы внести изменения используй клавиатуру внизу\.`'

    return text


async def del_temp_message(data: dict, msg: Message = None):
    if msg:
        await msg.delete()

    try:
        await data['temp'].delete()
    except TelegramBadRequest:
        pass
    except KeyError:
        pass


async def del_previous_message(data: dict, msg: Message = None):
    if msg:
        await msg.delete()

    try:
        await data['previous'].delete()
    except TelegramBadRequest:
        pass
    except KeyError:
        pass


def escape_string(string):
    characters_to_escape = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for character in characters_to_escape:
        string = string.replace(character, '\\' + character)
    return string
