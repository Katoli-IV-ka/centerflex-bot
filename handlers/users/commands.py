from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import IDFilter

from main import dp, bot

from aiogram.types import Message

from keyboards.reply.catalog import catalogMenuKb
from states.states import AddProductStates


@dp.message_handler(commands=['start', 'hi'], state='*')
async def get_start(msg: Message):
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo='AgACAgIAAxkBAAIEVGQVilHrcp5SrU4JeERzpNQiTwlgAAJpyTEbjFmpSPUyA_GeGK88AQADAgADeAADLwQ',
        caption='',
    )


@dp.message_handler(commands=['catalog'], state='*')
@dp.message_handler(text="Назад в меню", state='*')
async def get_start(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer(text='Catalog', reply_markup=catalogMenuKb)

@dp.message_handler(commands=['get_msg'], state='*')
async def get_start(msg: Message):
    message_text = ''
    for i in msg:
        message_text = message_text + str(i) + '\n\n'

    await msg.answer(
        text=message_text
    )
