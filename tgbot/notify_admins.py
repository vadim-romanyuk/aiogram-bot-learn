import logging

from aiogram import Dispatcher

from tgbot.config import Config
from tgbot.utils.db_api.postgresql import Database


async def on_startup_notify(dp: Dispatcher):
    config: Config = dp.bot.get('config')
    for admin in config.tg_bot.admin_ids:
        try:
            text = 'Бот запущен и готов к работе'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
