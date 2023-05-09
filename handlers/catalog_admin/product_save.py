from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from database import add_product
from handlers.catalog_admin.fuction import format_product_text
from keyboards.catalog_admin_keyboards import save_product_keyboard
from states.add_product import AddProductStates

router = Router()


@router.callback_query(Text('to_save_product'), AddProductStates.getPrice)
async def to_price_call(call: CallbackQuery, state: FSMContext):
    # чистим чат
    data = await state.get_data()
    await call.message.delete()
    try:
        await data['temp'].delete()
    except TelegramBadRequest:
        pass

    await state.set_state(AddProductStates.saveProduct)

    # сохраняем информацию о товаре в базу данных
    await add_product(
        title=data['product_title'],
        photo_id=data['product_photo_id'],
        description=data['product_description'],
        price=data['product_price'],
        display=data['product_display'],
    )

    await call.message.answer_photo(
        photo=data['product_photo_id'],
        parse_mode=ParseMode.MARKDOWN_V2,
        caption=format_product_text(data),
        reply_markup=save_product_keyboard()
    )


