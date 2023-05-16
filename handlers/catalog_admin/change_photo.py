from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from handlers.catalog_admin.utils import del_temp_message, del_previous_message, escape_string
from keyboards.catalog_admin_keyboards import next_step_keyboard, cancel_keyboard
from states.adminStates import ManageProductStates

router = Router()


@router.callback_query(Text('change_photo'), ManageProductStates.viewProduct)
async def change_photo(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await del_temp_message(data, call.message)

    await state.set_state(ManageProductStates.changePhoto)

    answer_msg = await call.message.answer(
        text='🖼 Загрузи новую фотографию товара',
        reply_markup=cancel_keyboard(back_to='manage_product')
    )

    await state.update_data(temp=answer_msg)


@router.message(F.photo, ManageProductStates.changePhoto)
async def confirm_change_photo(msg: Message, state: FSMContext):
    data = await state.get_data()

    await del_previous_message(data, msg)

    answer_msg = await msg.answer_photo(
        photo=msg.photo[-1].file_id,
        caption="*Новое фото загружена, сохранить?*\n"
                "\nЧтобы изменить, просто отправь новое фото",
        reply_markup=next_step_keyboard('save_photo_changes'),
        parse_mode=ParseMode.MARKDOWN_V2,
    )

    await state.update_data(previous=answer_msg, product_photo=msg.photo[-1].file_id)
