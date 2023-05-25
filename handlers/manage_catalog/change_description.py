from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from filters.id_filter import IsDescriptionMessage
from handlers.manage_catalog.utils import del_temp_message, del_previous_message, escape_string
from keyboards.manage_catalog.catalog_admin_keyboards import next_step_keyboard, cancel_keyboard
from states.adminStates import ManageProductStates

router = Router()


@router.callback_query(Text('change_description'), ManageProductStates.viewProduct)
async def change_description(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await del_temp_message(data, call.message)

    await state.set_state(ManageProductStates.changeDescription)

    answer_msg = await call.message.answer(
        text='📝 Введи новое описание товара',
        reply_markup=cancel_keyboard(back_to='manage_product')
    )

    await state.update_data(temp=answer_msg)


@router.message(F.text, ManageProductStates.changeDescription)
async def confirm_change_description(msg: Message, state: FSMContext):
    data = await state.get_data()

    await del_previous_message(data, msg)

    answer_msg = await msg.answer(
        text=f"*Новое описание добавленно*:\n`{escape_string(msg.text)}`\n"
             "\nЕсли нужно внести правки просто отправить новое сообщение или отредактируй старое",
        reply_markup=next_step_keyboard('save_description_changes'),
        parse_mode=ParseMode.MARKDOWN_V2,
    )

    await state.update_data(previous=answer_msg, product_description=escape_string(msg.text), description_message_temp=msg)


@router.edited_message(IsDescriptionMessage(), ManageProductStates.changeDescription)
async def confirm_edited_change_description(msg: Message, data: dict, state: FSMContext):
    try:
        await data['previous'].edit_text(
            text=f"*Новое описание добавленно*:\n`{escape_string(msg.text)}`\n"
                 "\nЕсли нужно внести правки просто отправить новое сообщение или отредактируй старое",
            reply_markup=next_step_keyboard('save_description_changes'),
            parse_mode=ParseMode.MARKDOWN_V2
        )
    except TelegramBadRequest:
        await msg.answer(
            text='😬 Извините произошёл сбой. Повторите отправку',
            reply_markup=cancel_keyboard()
        )

    await state.update_data(product_description=escape_string(msg.text))
