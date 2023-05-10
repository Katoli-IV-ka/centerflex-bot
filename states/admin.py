from aiogram.fsm.state import StatesGroup, State


class CatalogToolsStates(StatesGroup):
    getTitle = State()
    getPhoto = State()
    getDescription = State()
    getPrice = State()

    viewProduct = State()

    editTitle = State()
    editPhoto = State()
    editDescription = State()
    editPrice = State()

