from aiogram import Dispatcher
from handlers import all_handlers


def setup(dp: Dispatcher):
    for handler in all_handlers:
        dp.include_routers(handler)
