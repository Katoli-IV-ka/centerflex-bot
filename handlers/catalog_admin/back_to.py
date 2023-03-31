from aiogram.filters import Text

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from states.catalog_add_item import AddItemStates

router = Router()


@router.callback_query(Text('adm_to_menu'))
async def callback_adm_cancel(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer(text='adm cancel: В главное меню')


@router.callback_query(Text('adm_to_tittle'))
async def callback_adm_cancel(call: CallbackQuery, state: FSMContext):
    await state.set_state(AddItemStates.getTittle)
    await call.message.answer(text='to_Tittle: возвращаемся к добавлению tittle')
