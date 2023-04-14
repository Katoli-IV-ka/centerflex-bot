from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message

router = Router()


@router.callback_query(Text('edit_catalog'))
async def edit_catalog_call(msg: Message):
    await msg.answer(text="edit_catalog")


@router.callback_query(Text('add_to_catalog'))
async def add_to_catalog_call(msg: Message):
    await msg.answer(text="add_to_catalog")


@router.callback_query(Text('notification_queue'))
async def notification_queue_call(msg: Message):
    await msg.answer(text="notification_queue")


@router.callback_query(Text('edit_info'))
async def edit_info_call(msg: Message):
    await msg.answer(text="edit_info")
