from aiogram.fsm.state import StatesGroup, State


class AddProductStates(StatesGroup):
    getTitle = State()
    getPhoto = State()
    getDescription = State()
    getPrice = State()
    saveProduct = State()
