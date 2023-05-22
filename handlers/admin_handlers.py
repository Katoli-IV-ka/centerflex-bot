from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message

router = Router()


@router.callback_query(Text('edit_catalog'))
async def edit_catalog_call(msg: Message):
    await msg.answer(text="edit_catalog")
