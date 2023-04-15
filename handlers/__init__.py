from . import catalog_handlers, commands, admin_handlers, user_handlers
from .add_product import add_product_router

all_handlers = [
    catalog_handlers.router,
    commands.router,
    admin_handlers.router,
    user_handlers.router,
    add_product_router,
]
