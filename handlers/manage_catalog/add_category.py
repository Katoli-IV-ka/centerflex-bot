from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from database import add_category
from handlers.manage_catalog.get_photo import enter_photo
from handlers.utils import del_temp_message, escape_string, del_previous_message
from keyboards.manage_catalog.catalog_admin_keyboards import cancel_keyboard
from keyboards.manage_catalog.save_category_keyboard import save_category_keyboard
from states.adminStates import ManageProductStates

router = Router()


@router.callback_query(Text('catalog_add_category'))
async def enter_category_name(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await del_temp_message(data, call.message)

    await state.set_state(ManageProductStates.addCategories)

    answer_msg = await call.message.answer(
        text="✏ Введи название кетегории",
        reply_markup=cancel_keyboard()
    )

    await state.update_data(temp=answer_msg)


@router.message(F.text, ManageProductStates.addCategories)
async def confirm_category_name(msg: Message, state: FSMContext):
    data = await state.get_data()

    await del_previous_message(data, msg)

    try:
        answer_msg = await msg.answer(
            text=f"*Название категории*: _{escape_string(msg.text)}_\n"
                 "\nЧтобы внести изменения просто отправь новое название\.",
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=save_category_keyboard(),
        )
    except TelegramBadRequest:
        answer_msg = await msg.answer(
            text='😬 Извините произошёл сбой. Повторите отправку',
            reply_markup=cancel_keyboard()
        )

    await state.update_data(previous=answer_msg, new_category_name=msg.text)


@router.callback_query(Text('save_new_category'))
async def save_category(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = await state.get_data()

    category_id = await add_category(data['new_category_name'])
    answer_msg = await call.message.answer(
        text=f'Для товара выбрана категория: {data["new_category_name"]}'
    )

    await state.update_data(product_category_id=category_id, previous=answer_msg)

    await enter_photo(call=call, state=state)


