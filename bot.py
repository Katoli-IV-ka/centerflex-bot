import asyncio
from aiogram import Bot, Dispatcher

from handlers.catalog_admin.router import catalog_router
from handlers.commands import cmdRouter




async def main():
    bot = Bot(token="6244240330:AAGW-yNw74YBKVpAW4Np6J4QpLAIvsf0PB0")
    dp = Dispatcher()
    dp.include_routers(cmdRouter)
    dp.include_routers(catalog_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
