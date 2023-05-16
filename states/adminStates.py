from aiogram.fsm.state import StatesGroup, State


class ManageProductStates(StatesGroup):
    getTitle = State()
    getPhoto = State()
    getDescription = State()
    getPrice = State()

    viewProduct = State()

    changeTitle = State()
    changePhoto = State()
    changeDescription = State()
    changePrice = State()

