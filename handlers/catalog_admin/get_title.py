from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from handlers.catalog_admin.utils import del_previous_message, escape_string
from keyboards.catalog_admin_keyboards import next_step_keyboard, cancel_keyboard
from states.adminStates import ManageProductStates

router = Router()


@router.callback_query(Text('enter_title'))
async def enter_title(call: CallbackQuery, state: FSMContext):
    await state.clear()

    await state.set_state(ManageProductStates.getTitle)

    answer_msg = await call.message.answer(
        text="✏ Введи название товара:",
        reply_markup=cancel_keyboard()
    )

    await state.update_data(
        temp=answer_msg,
        product_title=None,
        product_photo=None,
        product_description=None,
        product_price=None,
        product_display=False,
        product_id=None,
    )


@router.message(F.text, ManageProductStates.getTitle)
async def confirm_title(msg: Message, state: FSMContext):
    data = await state.get_data()

    await del_previous_message(data, msg)

    try:
        answer_msg = await msg.answer(
            text=f"*Название товара*: _{escape_string(msg.text)}_\n"
                 "\nЧтобы внести изменения отредактируй сообщение или отправь новое\. Если всё верно, идём дальше 👟",
            reply_markup=next_step_keyboard(callback_data='enter_photo'),
            parse_mode=ParseMode.MARKDOWN_V2
        )
    except TelegramBadRequest:
        answer_msg = await msg.answer(
            text='😬 Извините произошёл сбой. Повторите отправку',
            reply_markup=cancel_keyboard()
        )

    await state.update_data(previous=answer_msg, product_title=escape_string(msg.text))

