from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.callback_datas import buy_callback

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='котлеты')
        ],
        [
            KeyboardButton(text='макароны'),
            KeyboardButton(text='кетчуп')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="купить грушу",
                                          callback_data=buy_callback.new(item_name='pear',
                                                                         quantity='1')
                                      ),
                                      InlineKeyboardButton(
                                          text="купить яблоки",
                                          callback_data='buy:apple:5'
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Отмена",
                                          callback_data='cancel'
                                      )
                                  ]
                              ])

pear_keyboard = InlineKeyboardMarkup()

PEAR_LINK = 'https://botfather.dev/dashboard/lesson/6-2-inlajn-knopki'
pear_link = InlineKeyboardButton(text='Купи тут', url=PEAR_LINK)
pear_keyboard.insert(pear_link)
