from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.catalog_admin.back_to import getBackToKb
from states.catalog_add_item import AddItemStates

router = Router()


@router.callback_query(Text('add_item'))
async def callback_add_item(call: CallbackQuery, state: FSMContext):
    await state.set_state(AddItemStates.getTittle)
    await state.update_data(
        photos=list(),
        trash=list(),
        tittle=None,
        caption=None,
        price=None,
        visability=False,
    )
    await call.message.answer(text='add-item:Как будет называтся товар?', reply_markup=getBackToKb())


