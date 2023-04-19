from aiogram import Router

from . import get_photo, get_title, get_description, get_price

add_product_router = Router()

add_product_router.include_routers(
    get_title.router,
    get_photo.router,
    get_description.router,
    get_price.router
)
