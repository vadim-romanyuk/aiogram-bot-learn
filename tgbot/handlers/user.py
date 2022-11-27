import logging
import re

from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from tgbot.filters.private_chat import IsPrivate
from tgbot.filters.test_filter import SomeF


async def user_filter(message: Message):
    await message.reply("It's filter private")


async def user_start(message: Message, middleware_data, from_filter):
    await message.answer(f"Hello, {message.from_user.full_name}\n{middleware_data=}\n{from_filter=}")
    logging.info(f"6. Handler")
    logging.info(f"Следующая точка: Post Process Message")
    return {"from_handler": "Данные их хендлера"}


async def user_help(message: Message):
    username = message.from_user.username
    await message.answer(f"May i help you? {username}")


async def user_settings(message: Message):
    username = message.from_user.username
    await message.answer(f"{username} ты нажал НАСТРОЙКИ")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_filter, IsPrivate(), text='123', state="*")
    dp.register_message_handler(user_start, SomeF(), commands=["start"], state="*")
    dp.register_message_handler(user_help, commands=["help"], state="*")
    dp.register_message_handler(user_settings, CommandStart(deep_link=re.compile(r'\d\d\d')))
