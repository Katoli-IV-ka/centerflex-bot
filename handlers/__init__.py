from . import catalog_handlers, commands, admin_handlers, user_handlers

all_handlers = [
    catalog_handlers.router,
    commands.router,
    admin_handlers.router,
    user_handlers.router,
]
