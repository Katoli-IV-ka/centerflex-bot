from aiogram import Router, F
from aiogram.filters import Text
from aiogram.types import Message, CallbackQuery

from states.adminStates import ManageProductStates

router = Router()


@router.callback_query(Text('catalog'))
async def edit_catalog_call(msg: Message):
    await msg.answer(text="catalog")


@router.callback_query(Text('fast_request'))
async def edit_catalog_call(msg: Message):
    await msg.answer(text="fast_request")


@router.callback_query(Text('about'))
async def edit_catalog_call(msg: Message):
    await msg.answer(text="about")
