from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery


from database import get_data
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
    products = await get_data()
    print(call.data.split('_')[-1])
    for i in products:
        await call.message.answer(
            text=str(i)
        )
