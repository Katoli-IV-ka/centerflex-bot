from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers.commands import cmd_start
from handlers.utils import get_product_text
from keyboards.view_catalog.catalog_category_keyboard import pages_keyboard
from states.userStates import ViewCatalogStates

router = Router()


@router.callback_query(Text('next_pages'), ViewCatalogStates.viewProductsPage)
async def catalog_choice_category(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    page = data['view_page']+1
    products = data['products_data']

    for i in products[page*2-2:page*2]:
        await call.message.answer_photo(
            photo=i['product_photo_id'],
            parse_mode=ParseMode.MARKDOWN_V2,
            caption=get_product_text(i),
        )

    await call.message.answer(
        text=f"Текущая страница: {page}",
        reply_markup=await pages_keyboard(),
    )

    await state.update_data(view_page=page)


@router.callback_query(Text('to_user_menu'))
async def catalog_choice_category(call: CallbackQuery, state: FSMContext):
    await cmd_start(state=state, msg=call.message)
