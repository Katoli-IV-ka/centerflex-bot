from aiogram import Router, F
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


@router.callback_query(Text(contains='cancel_add_product'))
async def edit_info_call(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    message_to_delete = call.data.split('-')[1]
    try:
        await data[message_to_delete].delete()
    except KeyError:
        pass

    await call.message.delete()
    await cmd_admin(msg=call.message, state=state)


@router.callback_query(Text('edit_info'))
async def edit_info_call(msg: Message):
    await msg.answer(text="edit_info")
