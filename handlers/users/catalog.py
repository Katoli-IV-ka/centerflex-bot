from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType, CallbackQuery

from keyboards.inline.catalog import cancelLoadPhotoKb
from keyboards.reply.catalog import loadPhotoKb, catalogMenuKb
from main import dp, bot
from aiogram.utils.exceptions import MessageToForwardNotFound, ChatNotFound

from states.to_add_products import AddProductStates


@dp.message_handler(text="Добавить товар", state='*')
async def _(msg: Message):
    await msg.delete()
    await msg.answer(text='Введите заголовок к товару')
    await AddProductStates.addTitleState.set()
    # Отменить добавление товара


# Ловлю заглавие товара
@dp.message_handler(content_types=ContentType.TEXT, state=AddProductStates.addTitleState)
async def _(msg: Message, state: FSMContext):
    await msg.answer(text='Теперь загрузите фотографии товара', reply_markup=loadPhotoKb)
    await AddProductStates.addPhotoState.set()
    await state.update_data(tittel=msg.text)
    await state.update_data(photo_msg_ids=[])


# Подчищает сообщения в состоянии загрузки заглавия
@dp.message_handler(content_types=ContentType.ANY, state=AddProductStates.addTitleState)
async def _(msg: Message):
    await msg.answer(text='Пожалуйста добавьте заголовок',)
    # Добавить клавиатуру "назад, оменить добавлени товара"


# Отлавливает загруженные фотографии
@dp.message_handler(content_types=ContentType.PHOTO, state=AddProductStates.addPhotoState)
async def _(msg: Message, state: FSMContext):
    photo = await state.get_data()
    photo_msg_ids = photo.get('photo_msg_ids')
    photo_msg_ids.append(msg.message_id)
    await state.update_data(photo_msg_ids=photo_msg_ids)
    # Возможность удалить фотографию и чтоб она не попала в каталог


# Сохраняем фотографии
@dp.message_handler(text="Cохранить фото", state=AddProductStates.addPhotoState)
async def _(msg: Message, state: FSMContext):
    await msg.answer(text='Фото добавлены, давайте добавим описание')
    photo = await state.get_data()
    photo_msg_ids = photo.get('photo_msg_ids')
    for id in photo_msg_ids:# ищем id сообщений которые уже удалены
        try:
            await bot.forward_message(chat_id=-0000, from_chat_id=msg.chat.id, message_id=id)
        except MessageToForwardNotFound:
            photo_msg_ids.remove(id)
            await state.update_data(photo_msg_ids=photo_msg_ids)
        except ChatNotFound:
            continue
    await AddProductStates.addCaptionState.set()


# Отмена загрузки фотографий
@dp.message_handler(text="Отменить загруку", state=AddProductStates.addPhotoState)
async def _(msg: Message, state: FSMContext):
    print('msg:\n', msg)
    await state.finish()
    await msg.answer(text='Catalog', reply_markup=catalogMenuKb)

# Инлайн клавиатура


# Не правильный ввод state = addPhoto
@dp.message_handler(content_types=ContentType.ANY, state=AddProductStates.addPhotoState)
async def _(msg: Message):
    await msg.answer(text='Пожалуйста загрузите фотографии товара без сжатия', reply_markup=cancelLoadPhotoKb)


# Отмена загрузки фотографий в инлайн клавиатуре
@dp.callback_query_handler(lambda c: c.data == 'cancel_load_photo', state=AddProductStates.addPhotoState)
async def _(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='Введите заголовок к товару')
    await AddProductStates.addTitleState.set()
    # Отменить добавление товара


@dp.callback_query_handler(lambda c: c.data == 'to_catalog_menu', state=AddProductStates.addPhotoState)
async def _(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer(text='Catalog', reply_markup=catalogMenuKb)


# Ловлю описание товара
@dp.message_handler(content_types=ContentType.TEXT, state=AddProductStates.addCaptionState)
async def _(msg: Message, state: FSMContext):
    await msg.answer(text='Описание добавлено, остаось указать ориентировочную цену',)
    await AddProductStates.addPriceState.set()
    # Запись данных в strogae
    # Кнопка не указывать цену


# Не правильный ввод описания
@dp.message_handler(content_types=ContentType.ANY, state=AddProductStates.addCaptionState)
async def _(msg: Message):
    await msg.answer(text='Пожалуйста добавьте описание к товару',)
    # Добавить клавиатуру 'Назад, Без описания'


# Ловлю цену товара
@dp.message_handler(content_types=ContentType.TEXT, state=AddProductStates.addPriceState)
async def _(msg: Message, state: FSMContext):
    await msg.answer(text='Товар успешно добавлен в каталог, вот как его увидят пользователи:',)
    await state.finish()
    # Запись данных в strogae
    # Отправка сформированой карточки товара








