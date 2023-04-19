from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers.add_product.fuction import make_text
from keyboards.admin_keyboards import save_product_keyboard
from states.add_product import AddProductStates

router = Router()


@router.callback_query(Text('to_save_product'), AddProductStates.getPrice)
async def to_price_call(call: CallbackQuery, state: FSMContext):
    # чистим чат
    data = await state.get_data()
    await call.message.delete()
    try:
        await data['to_price_temp'].delete()
    except TelegramBadRequest:
        pass

    await state.set_state(AddProductStates.saveProduct)

    product_info = []
    for key in ['product_photo_id', 'product_title', 'product_description', 'product_price']:
        try:
            product_info.append(data[key])
        except KeyError:
            continue

    await call.message.answer_photo(
        photo=data['product_photo_id'],
        parse_mode=ParseMode.MARKDOWN_V2,
        caption=make_text(data),
        reply_markup=save_product_keyboard()
    )


