def make_text(data: dict):
    text = f"*{data['product_title']}*"

    try:
        text += f"\n\n_{data['product_description']}_"
    except KeyError:
        pass

    try:
        text += f"\n\n Ориентировочная цена: *{data['product_price']}* руб\."
    except KeyError:
        pass

    text += '\n\n\n🛠 `Данное сообщение  - это представление того как товар отобразиться в каталоге\(без синей подписи). `'
    text += '`Чтобы внести изменения используй клавиатуру внизу\.`'

    return text
