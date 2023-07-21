from aiogram import Router

from . import products_categories, product_view
catalog_user_router = Router()

catalog_user_router.include_routers(
    products_categories.router,
    product_view.router,
)
