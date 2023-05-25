from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers.manage_catalog.get_photo import enter_photo
from handlers.manage_catalog.utils import del_temp_message, del_previous_message
from keyboards.manage_catalog.product_category_keyboard import product_category_keyboard
from states.adminStates import ManageProductStates

router = Router()


@router.callback_query(Text('enter_category'), ManageProductStates.getTitle)
async def enter_category(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await del_temp_message(data, call.message)

    await state.set_state(ManageProductStates.getCategory)

    answer_msg = await call.message.answer(
        text="🛒 Выберите категорию к которой отсноситься данный товар: \n"
             "\n_Если в списке нет подходящих категорий \- добавьте новую_",
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=await product_category_keyboard(),
    )

    await state.update_data(temp=answer_msg)


@router.callback_query(Text(contains='enter_category_'), ManageProductStates.getCategory)
async def confirm_category(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await del_previous_message(data, call.message)

    await call.answer(
        text="Категория выбрана"
    )

    await state.update_data(product_category_id=int(call.data.split('_')[-1]))

    await enter_photo(call=call, state=state)
