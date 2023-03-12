from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType, CallbackQuery

from keyboards.reply.catalog import loadPhotoKb
from main import dp

from states.to_add_products import AddProductStates


@dp.message_handler(text="Добавить товар", state='*')
async def _(msg: Message):
    await msg.delete()
    await msg.answer(text='Введите заголовок к товару')
    await AddProductStates.addTitleState.set()
    # Отменить добавление товара


@dp.message_handler(content_types=ContentType.TEXT, state=AddProductStates.addTitleState)
async def _(msg: Message, state: FSMContext):
    await msg.answer(text='Теперь загрузите фотографии товара', reply_markup=loadPhotoKb)
    await AddProductStates.addPhotoState.set()
    await state.update_data(tittel=msg.text)
    await state.update_data(photo=[])


@dp.message_handler(text="Cохранить фото", state=AddProductStates.addPhotoState)
async def _(msg: Message, state: FSMContext):
    await msg.answer(text='Фото добавлены, давайте добавим описание')
    print(await state.get_data())
    await AddProductStates.addCaptionState.set()


@dp.message_handler(content_types=ContentType.ANY, state=AddProductStates.addTitleState)
async def _(msg: Message):
    await msg.answer(text='Пожалуйста добавьте заголовок',)
    # Добавить клавиатуру "назад, оменить добавлени товара"


@dp.message_handler(content_types=ContentType.PHOTO, state=AddProductStates.addPhotoState)
async def _(msg: Message, state: FSMContext):
    photo = await state.get_data()
    photo = photo.get('photo')
    photo.append(msg.photo[0].file_unique_id)
    await state.update_data(photo=photo)
    print(await state.get_data())
    # Добавить клавиатуру "отменить загрузку, добавить фото"
    # Возможность удалить фотографию и чтоб она не попала в каталог


@dp.message_handler(content_types=ContentType.ANY, state=AddProductStates.addPhotoState)
async def _(msg: Message):
    await msg.answer(text='Пожалуйста загрузите фотографии товара без сжатия',)
    # Добавить клавиатуру "отменить загрузку"


@dp.message_handler(content_types=ContentType.TEXT, state=AddProductStates.addCaptionState)
async def _(msg: Message, state: FSMContext):
    await msg.answer(text='Описание добавлено, остаось указать ориентировочную цену',)
    await AddProductStates.addPriceState.set()
    # Запись данных в strogae
    # Кнопка не указывать цену


@dp.message_handler(content_types=ContentType.ANY, state=AddProductStates.addCaptionState)
async def _(msg: Message):
    await msg.answer(text='Пожалуйста добавьте описание к товару',)
    # Добавить клавиатуру 'Назад, Без описания'


@dp.message_handler(content_types=ContentType.TEXT, state=AddProductStates.addPriceState)
async def _(msg: Message, state: FSMContext):
    await msg.answer(text='Товар успешно добавлен в каталог, вот как его увидят пользователи:',)
    await state.finish()
    # Запись данных в strogae
    # Отправка сформированой карточки товара








