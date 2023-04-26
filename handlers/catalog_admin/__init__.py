from aiogram import Router

from . import get_photo, get_title, get_description, get_price, product_save, product_edit

add_product_router = Router()

add_product_router.include_routers(
    get_title.router,
    get_photo.router,
    get_description.router,
    get_price.router,
    product_save.router,
    product_edit.router
)
