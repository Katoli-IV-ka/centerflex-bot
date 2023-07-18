from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from handlers.utils import del_temp_message, del_previous_message
from keyboards.manage_catalog.catalog_admin_keyboards import next_step_keyboard, cancel_keyboard
from states.adminStates import ManageProductStates

router = Router()


@router.callback_query(Text('enter_photo'), ManageProductStates.getTitle)
async def enter_photo(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await del_temp_message(data)

    await state.set_state(ManageProductStates.getPhoto)

    answer_msg = await call.message.answer(
        text=f'🖼 Загрузи фотографию товара',
        reply_markup=cancel_keyboard())

    await state.update_data(temp=answer_msg)


@router.message(F.photo, ManageProductStates.getPhoto)
async def confirm_photo(msg: Message, state: FSMContext):
    data = await state.get_data()

    await del_previous_message(data, msg)

    try:
        answer_msg = await msg.answer_photo(
            photo=msg.photo[-1].file_id,
            caption="*Фотография загружена, сохранить?*\n"
                    "\nЧтобы изменить, просто отправь новое фото",
            reply_markup=next_step_keyboard(callback_data='enter_description', text='Далее  👟'),
            parse_mode=ParseMode.MARKDOWN_V2,
        )
    except TelegramBadRequest:
        answer_msg = await msg.answer(
            text='😬 Извините произошёл сбой. Повторите отправку',
            reply_markup=cancel_keyboard()
        )

    await state.update_data(previous=answer_msg, product_photo_id=msg.photo[-1].file_id)
