from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery

from keyboards.manage_catalog.catalog_admin_keyboards import save_product_keyboard

router = Router()


@router.callback_query(Text('change_display_hide'))
async def change_display_hide(call: CallbackQuery):
    await call.message.edit_reply_markup(
        reply_markup=save_product_keyboard(True)
    )


@router.callback_query(Text('change_display_show'))
async def change_display_show(call: CallbackQuery):
    await call.message.edit_reply_markup(
        reply_markup=save_product_keyboard()
    )

