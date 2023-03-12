from aiogram import Bot, executor, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN


storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)
