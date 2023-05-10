from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards.catalog_admin_keyboards import next_step_keyboard

router = Router()


@router.callback_query(Text('edit_text'))
async def to_edit_title(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    try:
        await data['temp'].delete()
    except TelegramBadRequest:
        pass
    except KeyError:
        pass

    await call.message.answer(
        text="✏ Введи новое название товара:"
    )


@router.message(F.text, )
async def get_title(msg: Message):
    await msg.answer(
        text='',
        reply_markup=next_step_keyboard('to_save_product')# не правильно так как будет пересохранять все данные
    )
