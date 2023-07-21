from aiogram.fsm.state import State, StatesGroup


class ViewCatalogStates(StatesGroup):
    viewProductsPage = State()
