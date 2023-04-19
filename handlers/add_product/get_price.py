from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards.admin_keyboards import cancel_keyboard, go_to_keyboard
from states.add_product import AddProductStates

router = Router()


@router.callback_query(Text('to_price'), AddProductStates.getDescription)
async def to_price_call(call: CallbackQuery, state: FSMContext):
    # чистим чат
    data = await state.get_data()
    await call.message.delete()
    try:
        await data['to_description_temp'].delete()
    except TelegramBadRequest:
        pass

    await state.set_state(AddProductStates.getPrice)

    answer_msg = await call.message.answer(
        text="💰 Укажи ориентировочную цену:",
        reply_markup=cancel_keyboard(data='get_price_temp', skip_to="to_save_product")
    )

    # получаем экземпляр сообщения для последующего удаления
    await state.update_data(to_price_temp=answer_msg)


@router.message(F.text, AddProductStates.getPrice)
async def get_price(msg: Message, state: FSMContext):
    # удаляем не нужные сообщения
    data = await state.get_data()
    await msg.delete()
    try:
        await data['get_price_temp'].delete()
    except KeyError:
        pass

    # получаем экземпляр сообщения для последующего удаления
    answer_msg = await msg.answer(
        text=f"*Ориентировочная цена:* _{msg.text}_"
             "\nЧтобы изменить отправь новое сообщение\.",
        reply_markup=go_to_keyboard(callback_data='to_save_product', text='Далее 🏁'),
        parse_mode=ParseMode.MARKDOWN_V2
    )

    # сохраняем полученные данные
    await state.update_data(product_price=msg.text, get_price_temp=answer_msg, price_message_temp=msg)
