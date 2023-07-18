from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from database import add_product, update_product_title, update_product_photo_id, update_product_description, \
    update_product_price, get_product
from handlers.utils import format_admin_product_text, del_temp_message
from keyboards.manage_catalog.catalog_admin_keyboards import save_product_keyboard
from states.adminStates import ManageProductStates

router = Router()


@router.callback_query(Text('manage_product'))
async def manage_product(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await del_temp_message(data, call.message)

    await state.set_state(ManageProductStates.viewProduct)

    product_data = await get_product(field_name='id', field_value=str(data['product_id']))

    await call.message.answer_photo(
        photo=product_data[-1]['product_photo_id'],
        parse_mode=ParseMode.MARKDOWN_V2,
        caption=format_admin_product_text(product_data[-1]),
        reply_markup=save_product_keyboard(product_data[-1]['product_display'])
    )


@router.callback_query(Text('save_all'))
async def save_product(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    product_id = await add_product(
        title=data['product_title'],
        photo_id=data['product_photo_id'],
        description=data['product_description'],
        price=data['product_price'],
        display=data['product_display'],
        category_id=data['product_category_id']
    )

    await state.update_data(product_id=product_id)
    await manage_product(call=call, state=state)


@router.callback_query(Text('save_title_changes'), ManageProductStates.changeTitle)
async def save_title(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await update_product_title(data['product_id'], data['product_title'])

    await manage_product(call=call, state=state)


@router.callback_query(Text('save_photo_changes'), ManageProductStates.changePhoto)
async def save_title(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await update_product_photo_id(data['product_id'], data['product_photo'])

    await manage_product(call=call, state=state)


@router.callback_query(Text('save_description_changes'), ManageProductStates.changeDescription)
async def save_title(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await update_product_description(data['product_id'], data['product_description'])

    await manage_product(call=call, state=state)


@router.callback_query(Text('save_price_changes'), ManageProductStates.changePrice)
async def save_title(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await update_product_price(data['product_id'], data['product_price'])

    await manage_product(call=call, state=state)



