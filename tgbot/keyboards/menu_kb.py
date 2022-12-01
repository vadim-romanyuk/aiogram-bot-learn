from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='котлеты')
        ],
        [
            KeyboardButton(text='макароны'),
            KeyboardButton(text='/form')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)