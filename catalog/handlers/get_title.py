from catalog.router import catalogRouter

from aiogram.types import Message, ContentType, CallbackQuery
from aiogram.dispatcher import FSMContext

from catalog.keyboards.get_photo import keyboardSavePhoto
from catalog.keyboards.to_menu import keyboardToMenu
from catalog.states import AddProductStates


@catalogRouter.message_handler(text="Добавить товар", state='*')
async def _(msg: Message):
    await msg.delete()
    await AddProductStates.getTittle.set()
    await msg.answer(text='Введите заголовок к товару')


@catalogRouter.message_handler(content_types=ContentType.TEXT, state=AddProductStates.getTittle)
async def _(msg: Message, state: FSMContext):
    await state.update_data(tittel=msg.text)
    await state.update_data(photo_msg_ids=[])
    await AddProductStates.getPhoto.set()
    await msg.answer(text='Теперь загрузите фотографии товара', reply_markup=keyboardSavePhoto)


@catalogRouter.message_handler(content_types=ContentType.ANY, state=AddProductStates.getTittle)
async def _(msg: Message):
    await msg.answer(text='Пожалуйста добавьте заголовок', reply_markup=keyboardToMenu)



