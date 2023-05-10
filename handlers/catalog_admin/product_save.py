from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from database import add_product
from handlers.catalog_admin.utils import format_product_text, del_temp_message
from keyboards.catalog_admin_keyboards import save_product_keyboard
from states.admin import CatalogToolsStates

router = Router()


@router.callback_query(Text('save_product'), CatalogToolsStates.getPrice)
async def to_price_call(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await del_temp_message(data, call.message)

    await state.set_state(CatalogToolsStates.viewProduct)

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


