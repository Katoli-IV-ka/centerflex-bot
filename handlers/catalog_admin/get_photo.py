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
    # Сохраняем id фото и id сообщения для удаления при следующем срабатывании
    await state.update_data(
        photos=await update_list(state, 'photos', msg.photo[-1].file_id),
        trash=await update_list(state, 'trash', msg.message_id+1),
    )
    # Сохраненние и переключение state
    await msg.answer_photo(
        caption='Первое фото:',
        photo=msg.photo[-1].file_id,
        reply_markup=getSaveKb("save_photo")
    )
    await state.set_state(AddItemStates.getSubsequentPhoto)
    await msg.delete()


@router.message(F.photo, AddItemStates.getSubsequentPhoto)
async def msg_add_photo(msg: Message, state: FSMContext, bot: Bot):
    # Удаляем сообщения с старым mediaGroup
    for trash_message in await get_value(state, 'trash'):
        await bot.delete_message(message_id=trash_message, chat_id=msg.chat.id)
    await state.update_data(trash=[])
    await msg.delete()

    # Сохраняем id фото и id сообщения для удаления при следующем срабатывании
    await state.update_data(
        photos=await update_list(state, 'photos', msg.photo[-1].file_id),
        trash=await update_list(state, 'trash', msg.message_id+1),
    )
    # Отправляем новый mediaGroup + вопрос о сохранении
    await msg.answer_media_group(media=await get_media(state=state))
    await msg.answer(
        text='Если всё верно жми сохранить',
        reply_markup=getSaveKb('save_photo')
    )


@router.callback_query(Text('save_photo'))
async def callback_save_tittle(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.clear()
    await call.message.answer(
        text='photo has saved: Опциональные поля',
        reply_markup=getOptionsKb(visibility=True)
    )

