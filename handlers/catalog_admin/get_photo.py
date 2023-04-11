from aiogram import Router, F, Bot
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from handlers.catalog_admin.fuction import update_list, get_value, get_media
from keyboards.catalog_admin.options import getOptionsKb
from keyboards.catalog_admin.save import getSaveKb
from states.catalog_add_item import AddItemStates

router = Router()


@router.message(F.photo, AddItemStates.getPhoto)
async def msg_add_photo(msg: Message, state: FSMContext):
    message = await get_value(state, 'photo_invitation')
    await message.edit_text(text=f'handlers/get_photo: Теперь загрузи фотографии товара\
        \n📷 загруженно фотографий: {int(message.text.split(" ")[-1])+1}')

    if msg.media_group_id is not None:
        print(msg.media_group_id)

    message = await message.edit_reply_markup(reply_markup=getSaveKb("save_photo"))
    await state.update_data(photo_invitation=message)
    await msg.delete()


@router.callback_query(Text('save_photo'))
async def callback_save_tittle(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.clear()
    await call.message.answer(
        text='photo has saved: Опциональные поля',
        reply_markup=getOptionsKb(visibility=True)
    )

