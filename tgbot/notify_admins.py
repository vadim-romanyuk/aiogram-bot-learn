import logging

from aiogram import Dispatcher

from config import Config


async def on_startup_notify(dp: Dispatcher):
    for admin in Config.tg_bot.admin_ids:
        try:
            text = 'Бот запущен и готов к работе'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)