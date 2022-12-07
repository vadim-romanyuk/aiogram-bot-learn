import emoji

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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

