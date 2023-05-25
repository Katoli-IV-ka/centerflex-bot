from aiogram import Router

from . import get_title, get_photo, get_description, get_price, \
    product_save, cancel_add_product, \
    change_title, change_photo, change_description, change_price, change_display, get_category, add_category

add_product_router = Router()

add_product_router.include_routers(
    cancel_add_product.router,
    add_category.router,

    get_title.router,
    get_photo.router,
    get_category.router,
    get_description.router,
    get_price.router,

    product_save.router,

    change_title.router,
    change_photo.router,
    change_description.router,
    change_price.router,
    change_display.router
)
