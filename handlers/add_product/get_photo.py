from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.admin_keyboards import to_title_keyboard, to_caption_keyboard
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
    answer_msg = await call.message.answer(text=f'🖼 Загрузи фотографию товара', reply_markup=to_title_keyboard())
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

    answer_msg = await msg.answer_photo(
        caption='*Фотография загружена, сохранить?*\n\n_Чтобы изменить, просто отправь новое фото_',
        reply_markup=to_caption_keyboard(),
        photo=msg.photo[-1].file_id,
        parse_mode=ParseMode.MARKDOWN_V2,
    )

    # сохраняем полученные данные
    await state.update_data(get_photo_temp=answer_msg, product_photo_id=msg.photo[-1].file_id)


