from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from filters.id_filter import IsDescriptionMessage
from keyboards.admin_keyboards import cancel_keyboard, go_to_keyboard
from states.add_product import AddProductStates

router = Router()


@router.callback_query(Text('to_description'), AddProductStates.getPhoto)
async def to_description_call(call: CallbackQuery, state: FSMContext):
    # чистим чат
    data = await state.get_data()
    await call.message.delete()
    try:
        await data['to_photo_temp'].delete()
    except TelegramBadRequest:
        pass

    await state.set_state(AddProductStates.getDescription)

    await call.message.answer(
        text=f'📝 Добавь описание товару',
        reply_markup=cancel_keyboard()
    )


@router.message(F.text, AddProductStates.getDescription)
async def get_title(msg: Message, state: FSMContext):
    # удаляем не нужные сообщения
    data = await state.get_data()
    try:
        await data['get_description_temp'].delete()
    except KeyError:
        pass

    # получаем экземпляр сообщения для последующего удаления
    answer_msg = await msg.answer(
        text=f"*Описание добавленно*:\n_{msg.text}_\n"
             "\nЕсли нужно внести правки просто отправить новое сообщение",
        reply_markup=go_to_keyboard(callback_data='to_price'),
        parse_mode=ParseMode.MARKDOWN_V2
    )

    # сохраняем полученные данные
    await state.update_data(product_description=msg.text, get_description_temp=answer_msg, description_message_temp=msg)


@router.edited_message(IsDescriptionMessage(), AddProductStates.getDescription)
async def edit_description_message(msg: Message, data: dict):
    await data['get_description_temp'].edit_text(
        text=f"*Описание добавленно*:\n_{msg.text}_\n"
             "\nЕсли нужно внести правки просто отправить новое сообщение",
        reply_markup=go_to_keyboard(callback_data='to_price'),
        parse_mode=ParseMode.MARKDOWN_V2
    )
