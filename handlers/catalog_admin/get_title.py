from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.catalog_admin_keyboards import go_to_keyboard, cancel_keyboard
from states.add_product import AddProductStates

router = Router()


@router.callback_query(Text('catalog_admin'))
async def add_product_call(call: CallbackQuery, state: FSMContext):
    await state.clear()

    await state.set_state(AddProductStates.getTitle)
    answer_msg = await call.message.answer(
        text="✏ Введи название товара:",
        reply_markup=cancel_keyboard('get_title_temp')
    )

    # получаем экземпляр сообщения для последующего удаления
    # добавляем пустое значениe для необезательных полей
    await state.update_data(
        add_product_temp=answer_msg,
        product_description=None,
        product_price=None,
        product_display=False,
    )


@router.message(F.text, AddProductStates.getTitle)
async def get_title(msg: Message, state: FSMContext):
    # чистим чат
    await msg.delete()
    data = await state.get_data()
    try:
        await data['get_title_temp'].delete()
    except KeyError:
        pass

    # получаем экземпляр сообщения для последующего удаления
    try:
        answer_msg = await msg.answer(
            text=f"*Название товара*:` {msg.text}`\n"
                 "\nЧтобы внести изменения отредактируй сообщение или отправь новое\. Если всё верно, идём дальше 👟",
            reply_markup=go_to_keyboard(callback_data='to_photo'),
            parse_mode=ParseMode.MARKDOWN_V2
        )
    except TelegramBadRequest:
        answer_msg = await msg.answer(
            text='😬 Извините произошёл сбой. Повторите отправку',
            reply_markup=cancel_keyboard()
        )

    # сохраняем полученные данные
    await state.update_data(product_title=msg.text, get_title_temp=answer_msg)
