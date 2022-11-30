import logging
import re

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.filters.private_chat import IsPrivate
from tgbot.filters.test_filter import SomeF
from tgbot.misc.throttling import rate_limit
from tgbot.models.models import User


async def user_filter(message: Message):
    await message.reply("It's filter private")


@rate_limit(5, key="start")
async def user_start(message: Message, middleware_data, from_filter, user: User):
    await message.answer(f"Hello, {message.from_user.full_name}\n{middleware_data=}\n{from_filter=}",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                         InlineKeyboardButton(
                                             text="Простая кнопка", callback_data="button")

                                 ]
                             ]
                         ))
    logging.info(f"6. Handler")
    logging.info(f"Следующая точка: Post Process Message")

    return {"from_handler": "Данные их хендлера"}


async def get_button(call: types.CallbackQuery):
    await call.message.answer('Вы нажали на кнопку')


async def user_help(message: Message):
    username = message.from_user.username
    await message.answer(f"May i help you? {username}")


async def user_settings(message: Message):
    username = message.from_user.username
    await message.answer(f"{username} ты нажал НАСТРОЙКИ")







def register_user(dp: Dispatcher):

    dp.register_message_handler(user_filter, IsPrivate(), text='123', state="*")
    dp.register_message_handler(user_start, SomeF(), commands=["start"], state="*")
    dp.register_callback_query_handler(get_button, text='button')
    dp.register_message_handler(user_help, commands=["help"], state="*")
    dp.register_message_handler(user_settings, CommandStart(deep_link=re.compile(r'\d\d\d')))

