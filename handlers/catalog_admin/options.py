from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.catalog_admin.back_to import getBackToKb, getBackToKb
from keyboards.catalog_admin.options import getOptionsKb
from states.catalog_add_item import AddItemStates

router = Router()


@router.callback_query(Text('adm_item_name'))
async def callback_adm_item_option_name(call: CallbackQuery, state: FSMContext):
    await state.set_state(AddItemStates.getTittleOptional)
    await call.message.answer(text='add-item:Как будет называтся товар?', reply_markup=getBackToKb(False, False, True))


@router.callback_query(Text('adm_item_photo'))
async def callback_adm_item_option_photo(call: CallbackQuery, state: FSMContext):
    await state.set_state(AddItemStates.getPhotoOptional)
    await call.message.answer(text='state getPhoto: Загрузите фотографию...', reply_markup=getBackToKb())


@router.callback_query(Text('adm_item_caption'))
async def callback_adm_item_option_caption(call: CallbackQuery):
    await call.message.answer('adm_item_caption')


@router.callback_query(Text('adm_item_price'))
async def callback_adm_item_option_price(call: CallbackQuery):
    await call.message.answer('adm_item_price')


@router.callback_query(Text('adm_item_show'))
async def callback_adm_item_option_price(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=getOptionsKb(True))


@router.callback_query(Text('adm_item_hide'))
async def callback_adm_item_option_price(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=getOptionsKb(False))

