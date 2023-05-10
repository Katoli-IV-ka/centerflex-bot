from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from handlers.commands import cmd_admin

router = Router()




@router.callback_query(Text('edit_catalog'))
async def edit_catalog_call(msg: Message):
    await msg.answer(text="edit_catalog")


@router.callback_query(Text('notification_queue'))
async def notification_queue_call(msg: Message):
    await msg.answer(text="notification_queue")


@router.callback_query(Text('edit_info'))
async def edit_info_call(msg: Message):
    await msg.answer(text="edit_info")



