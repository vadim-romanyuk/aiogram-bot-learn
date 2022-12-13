import logging
import re

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, BotCommandScopeChat
from aiogram.utils.markdown import quote_html

from tgbot.filters.private_chat import IsPrivate
from tgbot.filters.test_filter import SomeF
from tgbot.misc.throttling import rate_limit
from tgbot.models.models import User
from tgbot.services.setting_commands import set_starting_commands


async def user_filter(message: Message):
    await message.reply("It's filter private")


async def user_start(message: Message):
    await message.reply("hi")
    await set_starting_commands(message.bot, message.from_user.id)


async def message_get_commands(message: Message):
    no_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id))
    no_args = await message.bot.get_my_commands()
    en_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id), language_code='ru')
    await message.reply('\n\n'.join(
        f'<pre>{quote_html(arg)}</>' for arg in (no_args, no_lang, en_lang)
    ))


async def message_reset_commands(message: Message):
    await message.bot.delete_my_commands(BotCommandScopeChat(message.from_user.id), language_code='ru')
    await message.reply('команды удалены')


#
# @rate_limit(5, key="start")
# async def user_start(message: Message, middleware_data, from_filter, user: User):
#     await message.answer(f"Hello, {message.from_user.full_name}\n{middleware_data=}\n{from_filter=}",
#                          reply_markup=InlineKeyboardMarkup(
#                              inline_keyboard=[
#                                  [
#                                          InlineKeyboardButton(
#                                              text="Простая кнопка", callback_data="button")
#
#                                  ]
#                              ]
#                          ))
#     logging.info(f"6. Handler")
#     logging.info(f"Следующая точка: Post Process Message")
#
#     return {"from_handler": "Данные их хендлера"}


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
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(message_get_commands, commands=["get_commands"], state="*")
    dp.register_message_handler(message_reset_commands, commands=["reset_commands"], state="*")
    dp.register_callback_query_handler(get_button, text='button')
    dp.register_message_handler(user_help, commands=["help"], state="*")
    dp.register_message_handler(user_settings, CommandStart(deep_link=re.compile(r'\d\d\d')))
