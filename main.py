from aiogram import Bot, executor, Dispatcher

from config import BOT_TOKEN

from notification.scheldue import schedule_thread

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

if __name__ == "__main__":
    from dp import dp
    schedule_thread.start()
    executor.start_polling(dp, skip_updates=True)
