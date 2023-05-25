from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers.manage_catalog.utils import del_previous_message
from handlers.commands import cmd_admin

router = Router()


@router.callback_query(Text('cancel_add_product'))
async def edit_info_call(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await del_previous_message(data)

    await call.message.delete()
    await cmd_admin(msg=call.message, state=state)
