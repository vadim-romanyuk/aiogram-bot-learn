from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()


class UserInfo(StatesGroup):
    Name = State()
    Email = State()
    Phone = State()


class UserAnswers(StatesGroup):
    Answer = State()
