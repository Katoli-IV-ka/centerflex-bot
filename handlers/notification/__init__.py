from aiogram import Router

from . import notification_schedule

notification_router = Router()

notification_router.include_routers(
    notification_schedule.router
)

