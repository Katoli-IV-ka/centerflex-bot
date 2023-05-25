from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from filters.id_filter import IsDescriptionMessage
from handlers.manage_catalog.utils import del_previous_message, del_temp_message, escape_string
from keyboards.manage_catalog.catalog_admin_keyboards import cancel_keyboard, next_step_keyboard
from states.adminStates import ManageProductStates

router = Router()


@router.callback_query(Text('enter_description'), ManageProductStates.getPhoto)
async def enter_description(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await del_temp_message(data, call.message)

    await state.set_state(ManageProductStates.getDescription)

    answer_msg = await call.message.answer(
        text=f'📝 Добавь описание товару',
        reply_markup=cancel_keyboard(skip_to="enter_price")
    )

    await state.update_data(temp=answer_msg)


@router.message(F.text, ManageProductStates.getDescription)
async def confirm_description(msg: Message, state: FSMContext):
    data = await state.get_data()

    await del_previous_message(data)

    try:
        answer_msg = await msg.answer(
            text=f"*Описание добавленно*:\n _{escape_string(msg.text)}_\n"
                 "\nЕсли нужно внести правки просто отправить новое сообщение или отредактируй старое",
            reply_markup=next_step_keyboard(callback_data='enter_price', text='Далее  👟'),
            parse_mode=ParseMode.MARKDOWN_V2
        )
    except TelegramBadRequest:
        answer_msg = await msg.answer(
            text='😬 Извините произошёл сбой. Повторите отправку',
            reply_markup=cancel_keyboard()
        )

    await state.update_data(previous=answer_msg, product_description=escape_string(msg.text), description_message_temp=msg)


@router.edited_message(IsDescriptionMessage(), ManageProductStates.getDescription)
async def confirm_edited_description(msg: Message, data: dict, state: FSMContext):

    try:
        await data['previous'].edit_text(
            text=f"*Описание добавленно*:\n _{escape_string(msg.text)}_\n"
                 "\nЕсли нужно внести правки просто отправить новое сообщение или отредактируй старое",
            reply_markup=next_step_keyboard(callback_data='enter_price', text='Далее  👟'),
            parse_mode=ParseMode.MARKDOWN_V2
        )
    except TelegramBadRequest:
        await msg.answer(
            text='😬 Извините произошёл сбой. Повторите отправку',
            reply_markup=cancel_keyboard()
        )

    await state.update_data(product_description=escape_string(msg.text))
