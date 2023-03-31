from aiogram import Router

from handlers.catalog_admin import admin
from handlers.catalog_admin import get_tittle
from handlers.catalog_admin import get_photo
from handlers.catalog_admin import back_to
from handlers.catalog_admin import options

catalog_router = Router()

catalog_router.include_routers(
    admin.router,
    get_tittle.router,
    back_to.router,
    get_photo.router,
    options.router
)
