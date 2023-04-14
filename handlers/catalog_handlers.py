from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message

router = Router()


@router.callback_query(Text('catalog'))
async def edit_catalog_call(msg: Message):
    await msg.answer(text="catalog")
