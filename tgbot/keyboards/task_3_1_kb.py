import emoji

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.callback_datas import buys_callback, up_callback, down_callback

task_3_1_kb_in = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(
                                                  text="Купить товар",
                                                  callback_data=buys_callback.new(item_id='1',
                                                                                  item_name='1')
                                              )
                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  text=emoji.emojize(":thumbs_up:"),
                                                  callback_data='up'
                                              ),
                                              InlineKeyboardButton(
                                                  text=emoji.emojize(":thumbs_down:"),
                                                  callback_data='down'
                                              ),
                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  text="Поделиться с другом",
                                                  switch_inline_query=''
                                              )
                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  text="Отмена",
                                                  callback_data='cancel'

                                              )
                                          ],
                                      ])
