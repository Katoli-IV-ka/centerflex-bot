from aiogram import Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers.commands import cmd_admin

router = Router()


@router.callback_query(Text('cancel_add_product'))
async def edit_info_call(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    try:
        await data['previous'].delete()
    except TelegramBadRequest:
        pass
    except KeyError:
        pass

    await call.message.delete()
    await cmd_admin(msg=call.message, state=state)
