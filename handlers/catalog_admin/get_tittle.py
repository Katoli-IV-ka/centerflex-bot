from aiogram import Router, F
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.catalog_admin.back_to import getBackToKb
from keyboards.catalog_admin.save import getSaveKb
from states.catalog_add_item import AddItemStates

router = Router()


@router.message(F.text, AddItemStates.getTittle)
async def msg_add_tittle(msg: Message, state: FSMContext):
    await msg.delete()
    await state.update_data(tittle=msg.text)
    await msg.answer(
        text=f'Товар будет называться: {msg.text}\nЕсли всё верно жми 👇',
        reply_markup=getSaveKb('save_tittle')
    )


@router.callback_query(Text('save_tittle'))
async def callback_save_tittle(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.set_state(AddItemStates.getPhoto)
    message = await call.message.answer(
        text='handlers/get_tittle:Теперь загрузи фотографии товара  /n📷 загруженно фотографий: 0',
        reply_markup=getBackToKb(text='К названию', callback='add_item', cancel_button=True)
    )
    await state.update_data(photo_invitation=message)

