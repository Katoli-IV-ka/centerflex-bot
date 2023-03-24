from catalog.router import catalogRouter

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from catalog.states import AddProductStates


@catalogRouter.callback_query_handler(lambda c: c.data == 'to_menu', state=AddProductStates.getPhoto)
async def _(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text='to_menu')
    await state.finish()
