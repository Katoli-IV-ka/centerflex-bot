from main import dp

from aiogram.types import Message

from keyboards.reply.catalog import catalogMenuKb


@dp.message_handler(commands=['start', 'hi'])
async def get_start(msg: Message):
    await msg.answer(text='Hi')


@dp.message_handler(commands=['catalog'])
@dp.message_handler(text="Назад в меню")
async def get_start(msg: Message):
    await msg.answer(text='Catalog', reply_markup=catalogMenuKb)
