from aiogram import Router

from . import get_photo, get_title, get_description, get_price, product_save, cancel_add_product

add_product_router = Router()

add_product_router.include_routers(
    cancel_add_product.router,
    get_title.router,
    get_photo.router,
    get_description.router,
    get_price.router,
    product_save.router,
)
