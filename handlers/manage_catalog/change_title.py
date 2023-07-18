from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from handlers.utils import del_temp_message, del_previous_message, escape_string
from keyboards.manage_catalog.catalog_admin_keyboards import next_step_keyboard, cancel_keyboard
from states.adminStates import ManageProductStates

router = Router()


@router.callback_query(Text('change_title'), ManageProductStates.viewProduct)
async def change_title(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await del_temp_message(data, call.message)

    await state.set_state(ManageProductStates.changeTitle)

    answer_msg = await call.message.answer(
        text="✏ Введи новое название товара:",
        reply_markup=cancel_keyboard(back_to='manage_product')
    )

    await state.update_data(temp=answer_msg)



@router.message(F.text, ManageProductStates.changeTitle)
async def confirm_change_title(msg: Message, state: FSMContext):
    data = await state.get_data()

    await del_previous_message(data, msg)

    answer_msg = await msg.answer(
        text=f'*Новое название товара*: {escape_string(msg.text)}\n'
              '\n_Чтобы внести изменения отредактируй сообщение или отправь новое\. Если всё верно, идём дальше 👟_',
        reply_markup=next_step_keyboard('save_title_changes'),
        parse_mode=ParseMode.MARKDOWN_V2,
    )

    await state.update_data(previous=answer_msg, product_title=escape_string(msg.text))
