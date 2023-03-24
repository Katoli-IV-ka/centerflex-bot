from aiogram.dispatcher.filters.state import StatesGroup, State

class AddProductStates(StatesGroup):
    addTitleState = State()
    addPhotoState = State()
    addCaptionState = State()
    addPriceState = State()

