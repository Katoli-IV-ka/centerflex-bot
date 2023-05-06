from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.catalog_admin_keyboards import go_to_keyboard, cancel_keyboard
from states.add_product import AddProductStates

router = Router()


@router.callback_query(Text('to_photo'), AddProductStates.getTitle)
async def to_photo_call(call: CallbackQuery, state: FSMContext):
    # чистим чат
    data = await state.get_data()
    await call.message.delete()
    await data['add_product_temp'].delete()

    await state.set_state(AddProductStates.getPhoto)

    # сохраняем экземпляр сообщения для последующего удаления
    answer_msg = await call.message.answer(
        text=f'🖼 Загрузи фотографию товара',
        reply_markup=cancel_keyboard('get_photo_temp'))

    await state.update_data(to_photo_temp=answer_msg)


@router.message(F.photo, AddProductStates.getPhoto)
async def get_photo(msg: Message, state: FSMContext):
    # чистим чат
    data = await state.get_data()
    await msg.delete()
    try:
        await data['get_photo_temp'].delete()
    except KeyError:
        pass

    try:
        answer_msg = await msg.answer_photo(
            caption="*Фотография загружена, сохранить?*\n"
                    "\nЧтобы изменить, просто отправь новое фото",
            reply_markup=go_to_keyboard(callback_data='to_description', text='Далее  👟'),
            photo=msg.photo[-1].file_id,
            parse_mode=ParseMode.MARKDOWN_V2,
        )
    except TelegramBadRequest:
        answer_msg = await msg.answer(
            text='😬 Извините произошёл сбой. Повторите отправку',
            reply_markup=cancel_keyboard()
        )

    # сохраняем полученные данные
    await state.update_data(get_photo_temp=answer_msg, product_photo_id=msg.photo[-1].file_id)



