from catalog.router import catalogRouter

from aiogram.types import CallbackQuery

from catalog.states import AddProductStates


@catalogRouter.callback_query_handler(lambda c: c.data == 'edit_tittle', state=AddProductStates.addOption)
async def _(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='edit_tittle')


@catalogRouter.callback_query_handler(lambda c: c.data == 'edit_photo', state=AddProductStates.addOption)
async def _(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='edit_photo')


@catalogRouter.callback_query_handler(lambda c: c.data == 'edit_caption', state=AddProductStates.addOption)
async def _(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='edit_caption')


@catalogRouter.callback_query_handler(lambda c: c.data == 'edit_price', state=AddProductStates.addOption)
async def _(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='edit_price')


@catalogRouter.callback_query_handler(lambda c: c.data == 'view_in_catalog', state=AddProductStates.addOption)
async def _(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='view_in_catalog')


@catalogRouter.callback_query_handler(lambda c: c.data == 'hide_in_catalog', state=AddProductStates.addOption)
async def _(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='hide_in_catalog')
