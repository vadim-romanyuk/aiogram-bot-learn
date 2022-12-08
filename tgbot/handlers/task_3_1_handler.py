import logging

from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, CallbackQuery

from tgbot.config import load_config
from tgbot.keyboards.callback_datas import buys_callback
from tgbot.keyboards.task_3_1_kb import task_3_1_kb_in

config = load_config(".env")
caption = 'Пакупай товар номер'
bot = Bot(token=config.tg_bot.token)
photo_1 = InputFile("photos/kiwi.jpg")
photo_2 = InputFile("photos/strawberry.jpg")


# отправляем 2 фото с клавиатурами и подписью товара
async def show_menu_task_3_1(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=photo_1, caption=caption, reply_markup=task_3_1_kb_in)
    await bot.send_photo(chat_id=message.chat.id, photo=photo_2, caption=caption, reply_markup=task_3_1_kb_in)


# реакция на 'понравился товар'
async def show_thumbs_up(call: CallbackQuery):
    await call.answer("Тебе понравился этот товар")


# реакция на 'не понравился товар'
async def show_thumbs_down(call: CallbackQuery):
    await call.answer("Тебе не понравился этот товар")


# покупка товара
async def buy_product(call: CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60, show_alert=True)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    item_id = callback_data.get('item_id')
    await call.bot.edit_message_caption(caption=caption + f'{item_id}')


# УДАЛИТЬ!!!
async def cancel_buying(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    await call.answer("Вы отменили эту покупку!")
    # Вариант 1 - Отправляем пустую клваиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)


def register_show_menu_task_3_1(dp: Dispatcher):
    dp.register_message_handler(show_menu_task_3_1, Command('items'))
    dp.register_callback_query_handler(show_thumbs_up, text='up')
    dp.register_callback_query_handler(show_thumbs_down, text='down')
    dp.register_callback_query_handler(buy_product, buys_callback.filter(item_id='1'))

    dp.register_callback_query_handler(cancel_buying, text="cancel")
