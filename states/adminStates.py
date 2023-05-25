from aiogram.fsm.state import StatesGroup, State


class ManageProductStates(StatesGroup):
    addCategories = State()

    getTitle = State()
    getCategory = State()
    getPhoto = State()
    getDescription = State()
    getPrice = State()

    viewProduct = State()

    changeTitle = State()
    changeCategory = State()
    changePhoto = State()
    changeDescription = State()
    changePrice = State()

