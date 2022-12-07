from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from tgbot.keyboards.callback_datas import buy_callback

task_3_kb_in = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text="Edit Name",
                                                callback_data=buy_callback.new(item_name='pear',
                                                                               quantity='1')
                                            ),
                                            InlineKeyboardButton(
                                                text="Edit Description",
                                                callback_data=buy_callback.new(item_name='pear',
                                                                               quantity='1')
                                            ),
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text="Edit About",
                                                callback_data=buy_callback.new(item_name='pear',
                                                                               quantity='1')
                                            ),
                                            InlineKeyboardButton(
                                                text="Edit Botpic",
                                                callback_data=buy_callback.new(item_name='pear',
                                                                               quantity='1')
                                            ),
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text="Edit Commands",
                                                callback_data=buy_callback.new(item_name='pear',
                                                                               quantity='1')
                                            ),
                                            InlineKeyboardButton(
                                                text="<<Back to Bot",
                                                callback_data=buy_callback.new(item_name='pear',
                                                                               quantity='1')
                                            )
                                        ]
                                    ])

task_3_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="Edit Name"),

            KeyboardButton(
                text="Edit Description",
            ),
            KeyboardButton(
                text="Edit About",
            ),
            KeyboardButton(
                text="Edit Botpic",
            ),
            KeyboardButton(
                text="Edit Commands",
            ),
            KeyboardButton(
                text="<<Back to Bot",
            )
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
