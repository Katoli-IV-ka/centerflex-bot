from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from handlers.utils import del_temp_message, del_previous_message, escape_string
from keyboards.manage_catalog.catalog_admin_keyboards import cancel_keyboard, next_step_keyboard
from states.adminStates import ManageProductStates

router = Router()


@router.callback_query(Text('enter_price'), ManageProductStates.getDescription)
async def enter_price(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    # удаляем сообщение с описанием, так как оно оставлялось для возможного редактирования
    try:
        await data['description_message_temp'].delete()
    except KeyError:
        pass

    await del_temp_message(data, call.message)

    await state.set_state(ManageProductStates.getPrice)

    answer_msg = await call.message.answer(
        text="💰 Укажи ориентировочную цену:",
        reply_markup=cancel_keyboard(skip_to="save_all")
    )

    await state.update_data(temp=answer_msg)


@router.message(F.text, ManageProductStates.getPrice)
async def confirm_price(msg: Message, state: FSMContext):

    data = await state.get_data()

    await del_previous_message(data, msg)

    answer_msg = await msg.answer(
        text=f"*Ориентировочная цена:* _{escape_string(msg.text)}_"
             "\nЧтобы изменить отправь новое сообщение\.",
        reply_markup=next_step_keyboard(callback_data='save_all', text='Далее 🏁'),
        parse_mode=ParseMode.MARKDOWN_V2
    )

    await state.update_data(previous=answer_msg, product_price=escape_string(msg.text))
