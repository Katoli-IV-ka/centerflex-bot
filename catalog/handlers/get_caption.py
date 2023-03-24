from catalog.router import catalogRouter

from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, Message

from catalog.states import AddProductStates


@catalogRouter.message_handler(content_types=ContentType.TEXT, state=AddProductStates.getCaption)
async def _(msg: Message):
    await msg.answer(text='Установить цену',)
    await AddProductStates.getCaption.set()
    # Запись данных в strogae
    # Кнопка не указывать цену


@catalogRouter.message_handler(content_types=ContentType.ANY, state=AddProductStates.getCaption)
async def _(msg: Message):
    await msg.answer(text='Пожалуйста добавьте описание к товару')