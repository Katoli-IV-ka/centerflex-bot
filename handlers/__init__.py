from . import  commands, admin_handlers, user_handlers, notification

from .catalog_admin import add_product_router
from .notification import notification_router

all_handlers = [
    commands.router,
    admin_handlers.router,
    user_handlers.router,

    add_product_router,
    notification_router,
]
