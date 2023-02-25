from main import dp, bot

from aiogram import types

from menu.menu_kb import mainMenuKb


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Hi',
        reply_markup=mainMenuKb
    )




