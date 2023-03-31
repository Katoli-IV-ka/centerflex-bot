from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.catalog_admin.admin import getCatalogAdminKb

cmdRouter = Router()


@cmdRouter.message(Command('start'))
async def cmd_start(msg: Message):
    await msg.answer(text='cmd_start')


@cmdRouter.message(Command('admin'))
async def cmd_admin(msg: Message):
    await msg.answer(text='cmd_admin', reply_markup=getCatalogAdminKb())


