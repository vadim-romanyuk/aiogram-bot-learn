import re

from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message


async def user_start(message: Message):
    await message.reply("Hello, user!")


async def user_help(message: Message):
    username = message.from_user.username
    await message.answer(f"May i help you? {username}")


async def user_settings(message: Message):
    username = message.from_user.username
    await message.answer(f"{username} ты нажал НАСТРОЙКИ")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(user_help, commands=["help"], state="*")
    dp.register_message_handler(user_settings, CommandStart(deep_link=re.compile(r'\d\d\d')))

