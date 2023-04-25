def make_text(data: dict):
    text = f"*{data['product_title']}*"

    if data['product_description']:
        text += f"\n\n_{data['product_description']}_"

    if data['product_price']:
        text += f"\n\nОриентировочная цена: *{data['product_price']}* руб\."

    text += '\n\n\n🛠` Данное сообщение - это представление того как товар отобразиться в каталоге\ (без этой подписи). `'
    text += '`Чтобы внести изменения используй клавиатуру внизу\.`'

    return text
