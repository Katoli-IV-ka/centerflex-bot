from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InputMediaPhoto

from database import get_product
from handlers.utils import get_product_text
from handlers.view_catalog.products_categories import catalog_choice_category
from keyboards.view_catalog.catalog_category_keyboard import product_keyboard, last_product_keyboard, \
    first_product_keyboard

router = Router()


@router.callback_query(Text(contains='next_product_'))
async def to_next_product(call: CallbackQuery):
    _, _, category_id, product_id = call.data.split('_')
    current_product_id = int(product_id) + 1
    products = await get_product('category_id', category_id)

    if len(products)-1 <= current_product_id:
        await call.message.edit_media(
            media=InputMediaPhoto(
                media=products[current_product_id]['product_photo_id'],
                caption=get_product_text(products[current_product_id]),
            ),
            reply_markup=await last_product_keyboard(f"product_{category_id}_{current_product_id}")
        )

    else:
        await call.message.edit_media(
            media=InputMediaPhoto(
                media=products[current_product_id]['product_photo_id'],
                caption=get_product_text(products[current_product_id]),
            ),
            reply_markup=await product_keyboard(f"product_{category_id}_{current_product_id}")
        )


@router.callback_query(Text(contains='previous_product_'))
async def to_previous_product(call: CallbackQuery):
    _, _, category_id, product_id = call.data.split('_')
    current_product_id = int(product_id) - 1
    products = await get_product('category_id', category_id)

    if 0 >= current_product_id:
        await call.message.edit_media(
            media=InputMediaPhoto(
                media=products[current_product_id]['product_photo_id'],
                caption=get_product_text(products[current_product_id]),
            ),
            reply_markup=await first_product_keyboard(f"product_{category_id}_{current_product_id}")
        )

    else:
        await call.message.edit_media(
            media=InputMediaPhoto(
                media=products[current_product_id]['product_photo_id'],
                caption=get_product_text(products[current_product_id]),
            ),
            reply_markup=await product_keyboard(f"product_{category_id}_{current_product_id}")
        )


@router.callback_query(Text('to_chocie_category'))
async def to_catalog_choice_category(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await catalog_choice_category(call=call)
