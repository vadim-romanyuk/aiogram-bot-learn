import emoji
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.callback_datas import buys_callback, down_callback, up_callback, sell_callback

# функция клавиатуры, для выдачи переменной
def buy_keyboard(item_id):
    task_3_1_kb_in = InlineKeyboardMarkup(row_width=2,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(
                                                      text="Купить товар",
                                                      callback_data=buys_callback.new(item_id=f'{item_id}'),
                                                  )
                                              ],
                                              [
                                                  InlineKeyboardButton(
                                                      text=emoji.emojize(":thumbs_up:"),
                                                      callback_data=up_callback.new(item_id=f'{item_id}'),
                                                  ),
                                                  InlineKeyboardButton(
                                                      text=emoji.emojize(":thumbs_down:"),
                                                      callback_data=down_callback.new(item_id=f'{item_id}'),
                                                  ),
                                              ],
                                              [
                                                  InlineKeyboardButton(
                                                      text="Поделиться с другом",
                                                      switch_inline_query=sell_callback.new(item_id=f'{item_id}'),
                                                  )
                                              ],
                                              [
                                                  InlineKeyboardButton(
                                                      text="Отмена",
                                                      callback_data='cancel'

                                                  )
                                              ],
                                          ])
    return task_3_1_kb_in




