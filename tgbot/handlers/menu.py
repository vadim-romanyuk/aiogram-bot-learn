import logging

from aiogram import types, Dispatcher


from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery


from tgbot.keyboards.callback_datas import buy_callback
from tgbot.keyboards.menu_kb import menu, choice, pear_keyboard


async def show_menu(message: types.Message):
    await message.answer('Выберите товар', reply_markup=menu)


async def get_text_button(message: types.Message):
    await message.answer('Вы выбрали макароны')


async def get_food(message: types.Message):
    await message.answer(f'Вы выбрали {message.text}', reply_markup=ReplyKeyboardRemove())


async def show_items(message: types.Message):
    await message.answer(text='на продажу у нас есть 2 товара: 5 яблок и 1 груша\n'
                              'если ничего не нужно - жми отмену',
                         reply_markup=choice, )


async def buying_pear(call: CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60, show_alert=True)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'вы выбрали грушу, всего {quantity}',
                              reply_markup=pear_keyboard,
                              )


# async def cancel(call: CallbackQuery):
#     await call.answer(text='вы отменили', show_alert=True)
#     await call.message.edit_reply_markup()

async def cancel_buying(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    await call.answer("Вы отменили эту покупку!", show_alert=True)
    # Вариант 1 - Отправляем пустую клваиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)


def register_menu(dp: Dispatcher):
    dp.register_message_handler(show_menu, Command('menu'))
    dp.register_message_handler(get_text_button, text='макароны')
    dp.register_message_handler(get_food, Text(equals=['макароны', 'кетчуп']))
    dp.register_message_handler(show_items, Command('items'))
    dp.register_callback_query_handler(buying_pear, buy_callback.filter(item_name='pear'))
    dp.register_callback_query_handler(cancel_buying, text="cancel")




