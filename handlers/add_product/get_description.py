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
    await data['to_photo_temp'].delete()

    await state.set_state(AddProductStates.getDescription)

    answer_msg = await call.message.answer(
        text=f'📝 Добавь описание товару',
        reply_markup=cancel_keyboard(data='get_description_temp', skip_to="to_price")
    )

    await state.update_data(to_description_temp=answer_msg)


@router.message(F.text, AddProductStates.getDescription)
async def get_description(msg: Message, state: FSMContext):
    # чистим чат
    data = await state.get_data()
    await msg.delete()
    try:
        await data['get_description_temp'].delete()
    except KeyError:
        pass

    # получаем экземпляр сообщения для последующего удаления
    try:
        answer_msg = await msg.answer(
            text=f"*Описание добавленно*:\n`{msg.text}`\n"
                 "\nЕсли нужно внести правки просто отправить новое сообщение или отредактируй старое",
            reply_markup=go_to_keyboard(callback_data='to_price', text='Далее  👟'),
            parse_mode=ParseMode.MARKDOWN_V2
        )
    except TelegramBadRequest:
        await msg.answer(
            text='😬 Извините произошёл сбой. Повторите отправку',
            reply_markup=cancel_keyboard()
        )

    # сохраняем полученные данные
    await state.update_data(product_description=msg.text, get_description_temp=answer_msg, description_message_temp=msg)


@router.edited_message(IsDescriptionMessage(), AddProductStates.getDescription)
async def edit_description_message(msg: Message, data: dict):

    try:
        await data['get_description_temp'].edit_text(
            text=f"*Описание добавленно*:\n`{msg.text}`\n"
                 "\nЕсли нужно внести правки просто отправить новое сообщение или отредактируй старое",
            reply_markup=go_to_keyboard(callback_data='to_price', text='Далее  👟'),
            parse_mode=ParseMode.MARKDOWN_V2
        )
    except TelegramBadRequest:
        await msg.answer(
            text='😬 Извините произошёл сбой. Повторите отправку',
            reply_markup=cancel_keyboard()
        )