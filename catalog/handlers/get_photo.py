from main import bot
from catalog.router import catalogRouter

from aiogram.utils.exceptions import ChatNotFound, MessageToForwardNotFound
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, Message, CallbackQuery

from catalog.states import AddProductStates
from catalog.keyboards.to_menu import keyboardToMenu


@catalogRouter.message_handler(content_types=ContentType.PHOTO, state=AddProductStates.getPhoto)
async def _(msg: Message, state: FSMContext):
    photo = await state.get_data()
    photo_msg_ids = photo.get('photo_msg_ids')
    photo_msg_ids.append(msg.message_id)
    await state.update_data(photo_msg_ids=photo_msg_ids)


@catalogRouter.message_handler(text="Cохранить фото", state=AddProductStates.getPhoto)
async def _(msg: Message, state: FSMContext):
    await msg.delete()
    await AddProductStates.getCaption.set()
    await msg.answer(text='Фото добавлены, давайте добавим описание', reply_markup=keyboardToOption)

    photo = await state.get_data()
    photo_msg_ids = photo.get('photo_msg_ids')
    for id in photo_msg_ids:  # ищем id сообщений которые уже удалены
        try:
            await bot.forward_message(chat_id=-0000, from_chat_id=msg.chat.id, message_id=id)
        except MessageToForwardNotFound:
            photo_msg_ids.remove(id)
            await state.update_data(photo_msg_ids=photo_msg_ids)
        except ChatNotFound:
            continue


@catalogRouter.message_handler(text="Назад к названию", state=AddProductStates.getPhoto)
async def _(msg: Message):
    await msg.delete()
    await AddProductStates.getTittle.set()
    await msg.answer(text='Введите заголовок к товару')


@catalogRouter.message_handler(text="Не добавлять товар", state=AddProductStates.getPhoto)
async def _(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer(text='Здесь должно быть перенаправление в главное меню')


@catalogRouter.message_handler(content_types=ContentType.ANY, state=AddProductStates.getPhoto)
async def _(msg: Message):
    await msg.answer(text='Пожалуйста загрузите фотографии товара без сжатия', reply_markup=keyboardToMenu)
