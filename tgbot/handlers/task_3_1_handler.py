import logging

from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, CallbackQuery

from tgbot.config import load_config
from tgbot.data.items_data_task3 import fruits
from tgbot.keyboards.callback_datas import buys_callback, down_callback, up_callback
from tgbot.keyboards.task_3_1_kb import buy_keyboard

config = load_config(".env")
bot = Bot(token=config.tg_bot.token)


# вывожу циклом все товары
async def show_menu_task_3_1(message: types.Message):
    for fruit in fruits:
        # await bot.send_photo(chat_id=message.chat.id, photo=fruit.photo_link, caption=fruit.name,
        #                      reply_markup=task_3_1_kb_in)
        await message.answer_photo(
            photo=fruit.photo_link,
            caption=fruit.name,
            reply_markup=buy_keyboard(item_id=fruit.item_id)
        )


# покупка товара
async def buy_product(call: CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60, show_alert=True)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    item_id = callback_data.get('item_id')

    await call.bot.edit_message_caption(caption=f'Покупай товар номер {item_id}', chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)


# реакция на 'понравился товар'
async def show_thumbs_up(call: CallbackQuery):
    await call.answer("Тебе понравился этот товар")


# реакция на 'не понравился товар'
async def show_thumbs_down(call: CallbackQuery):
    await call.answer("Тебе не понравился этот товар")


# УДАЛИТЬ!!!
async def cancel_buying(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    await call.answer("Вы отменили эту покупку!")
    # Вариант 1 - Отправляем пустую клваиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)


def register_show_menu_task_3_1(dp: Dispatcher):
    dp.register_message_handler(show_menu_task_3_1, Command('items'))
    dp.register_callback_query_handler(show_thumbs_up, up_callback.filter())
    dp.register_callback_query_handler(show_thumbs_down, down_callback.filter())
    dp.register_callback_query_handler(buy_product, buys_callback.filter())


    dp.register_callback_query_handler(cancel_buying, text="cancel")
