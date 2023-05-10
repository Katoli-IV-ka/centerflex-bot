from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from handlers.catalog_admin.utils import del_previous_message
from keyboards.catalog_admin_keyboards import next_step_keyboard, cancel_keyboard
from states.admin import CatalogToolsStates

router = Router()


@router.callback_query(Text('enter_title'))
async def enter_title(call: CallbackQuery, state: FSMContext):
    await state.clear()

    await state.set_state(CatalogToolsStates.getTitle)

    answer_msg = await call.message.answer(
        text="✏ Введи название товара:",
        reply_markup=cancel_keyboard()
    )

    await state.update_data(
        temp=answer_msg,
        product_description=None,
        product_price=None,
        product_display=False,
    )


@router.message(F.text, CatalogToolsStates.getTitle)
async def confirm_title(msg: Message, state: FSMContext):
    data = await state.get_data()

    await del_previous_message(data, msg)

    try:
        answer_msg = await msg.answer(
            text=f"*Название товара*:` {msg.text}`\n"
                 "\nЧтобы внести изменения отредактируй сообщение или отправь новое\. Если всё верно, идём дальше 👟",
            reply_markup=next_step_keyboard(callback_data='enter_photo'),
            parse_mode=ParseMode.MARKDOWN_V2
        )
    except TelegramBadRequest:
        answer_msg = await msg.answer(
            text='😬 Извините произошёл сбой. Повторите отправку',
            reply_markup=cancel_keyboard()
        )

    await state.update_data(previous=answer_msg, product_title=msg.text)
