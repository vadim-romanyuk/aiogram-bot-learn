import logging

from aiogram import Dispatcher

from tgbot.config import Config, DbConfig
from tgbot.infrastucture.database.functions.setup import create_session_pool


async def on_startup_notify(dp: Dispatcher):
    config: Config = dp.bot.get('config')
    for admin in config.tg_bot.admin_ids:
        try:
            text = 'Бот запущен и готов к работе'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)




