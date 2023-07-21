from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery


from database import get_product
from handlers.utils import get_product_text
from keyboards.view_catalog.catalog_category_keyboard import categories_keyboard, pages_keyboard
from states.userStates import ViewCatalogStates

router = Router()


@router.callback_query(Text('catalog'))
async def catalog_choice_category(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        text='Выберите категорию',
        reply_markup=await categories_keyboard()
    )

    await state.set_state(ViewCatalogStates.viewProductsPage)


@router.callback_query(Text(contains='catalog_category_'), ViewCatalogStates.viewProductsPage)
async def catalog_all_products(call: CallbackQuery, state: FSMContext):
    products = await get_product('category_id', call.data.split('_')[-1])
    page = 1
    await state.update_data(view_page=page, products_data=products)

    if products is None:
        await call.message.answer(
            text='К сожелению в данной категории нет доступных товаров ' 
            'Вы можете выбрать другую категорию'
        )
        return None

    if len(products) < 3:
        for i in products[page * 2 - 2:page * 2]:
            await call.message.answer_photo(
                photo=i['product_photo_id'],
                parse_mode=ParseMode.MARKDOWN_V2,
                caption=get_product_text(i),
            )

        return None

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
