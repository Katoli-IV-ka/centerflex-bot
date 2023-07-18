from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Text
from aiogram.types import CallbackQuery


from database import get_product
from handlers.utils import get_product_text
from keyboards.catalog_user.catalog_category_keyboard import categories_keyboard

router = Router()


@router.callback_query(Text('catalog'))
async def catalog_choice_category(call: CallbackQuery):
    await call.message.answer(
        text='Выберите категорию',
        reply_markup=await categories_keyboard()
    )


@router.callback_query(Text(contains='catalog_category_'))
async def catalog_all_products(call: CallbackQuery):
    products = await get_product('category_id', call.data.split('_')[-1])

    if products is None:
        await call.message.answer(
            text='К сожелению в данной категории нет доступных товаров ' 
            'Вы можете выбрать другую категорию'
        )
        return None

    for i in products:
        await call.message.answer_photo(
            photo=i['product_photo_id'],
            parse_mode=ParseMode.MARKDOWN_V2,
            caption=get_product_text(i),
        )
