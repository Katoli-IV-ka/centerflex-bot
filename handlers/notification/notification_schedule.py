from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery

from keyboards.notification.notification_control import notification_control_keyboard

router = Router()


@router.callback_query(Text('notification_control'))
async def notification_control_call(call: CallbackQuery):
    await call.message.answer(
        text="1️⃣ Краска модная\n"
             "Длинное описание можной краски для примера ещё пару слов текста чтоб было похоже\n\n"
             "2️⃣ Наждачка не модная\n"
             "Ещё одно не очень длинное описание можной наждачки для примера ещё бы текст придумывать самостоятельсно "
             "вместо использования Lauren Ipsum\n",
        reply_markup=notification_control_keyboard()
    )





