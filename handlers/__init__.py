from . import  commands, admin_handlers, user_handlers
from .catalog_admin import add_product_router

all_handlers = [
    commands.router,
    admin_handlers.router,
    user_handlers.router,
    add_product_router,
]
