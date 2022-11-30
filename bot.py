import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config, TgBot, Config
from tgbot.filters.admin import AdminFilter
from tgbot.filters.private_chat import IsPrivate
from tgbot.handlers.admin import register_admin, admin_start
from tgbot.handlers.echo import register_echo
from tgbot.handlers.user import register_user
from tgbot.handlers.acl_test import register_acl_test
from tgbot.handlers.testing import register_testing
from tgbot.handlers.info_user import register_info_user
from tgbot.middlewares.environment import EnvironmentMiddleware
from tgbot.middlewares.big_brother import BigBrother
from tgbot.middlewares.thottling import ThrotlingMiddleware
from tgbot.middlewares.acl import ACLMiddleware
from tgbot.middlewares.sentinel import Sentinel

logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):
    dp.setup_middleware(EnvironmentMiddleware(config=config))
    dp.setup_middleware(ACLMiddleware())
    dp.setup_middleware(BigBrother())
    dp.setup_middleware(ThrotlingMiddleware())
    dp.setup_middleware(Sentinel())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsPrivate)


def register_all_handlers(dp):
    register_admin(dp)
    register_user(dp)
    register_testing(dp)
    register_acl_test(dp)
    register_info_user(dp)

    register_echo(dp)


async def on_startup_notify(dp: Dispatcher):
    for admin in Config.tg_bot.admin_ids:
        try:
            text = 'Бот запущен и готов к работе'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)



async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")


    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.skip_updates()
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()








if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
