from . import  commands, admin_handlers, user_handlers, notification

from .manage_catalog import add_product_router
from .notification import notification_router
from .view_catalog import catalog_user_router

all_handlers = [
    commands.router,
    admin_handlers.router,
    user_handlers.router,

    add_product_router,
    notification_router,
    catalog_user_router,
]
