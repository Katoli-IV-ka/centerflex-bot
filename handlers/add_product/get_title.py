from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.admin_keyboards import to_admin_keyboard, to_photo_keyboard
from states.add_product import AddProductStates

router = Router()


@router.callback_query(Text('add_product'))
async def add_product_call(call: CallbackQuery, state: FSMContext):
    await state.set_state(AddProductStates.getTitle)
    answer_msg = await call.message.answer(text="📝 Введи название товара:")

    # получаем экземпляр сообщения для последующего удаления
    await state.update_data(add_product_temp=answer_msg)


@router.message(F.text, AddProductStates.getTitle)
async def get_title(msg: Message, state: FSMContext):
    # удаляем не нужные сообщения
    await msg.delete()
    data = await state.get_data()
    try:
        await data['get_title_temp'].delete()
    except KeyError:
        pass

    # получаем экземпляр сообщения для последующего удаления
    answer_msg = await msg.answer(
        text=f"*Название товара*: _{msg.text}_\n\nЕсли всё верно идём дальше",
        reply_markup=to_photo_keyboard(),
        parse_mode=ParseMode.MARKDOWN_V2
    )

    # сохраняем полученные данные
    await state.update_data(product_title=msg.text, get_title_temp=answer_msg)
