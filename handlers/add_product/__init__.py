from aiogram import Router

from . import get_photo, get_title, get_description

add_product_router = Router()
add_product_router.include_routers(get_photo.router, get_title.router, get_description.router)
