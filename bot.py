import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.config import load_config, Config
from tgbot.filters.admin import AdminFilter
from tgbot.filters.private_chat import IsPrivate
from tgbot.handlers.acl_test import register_acl_test
from tgbot.handlers.admin import register_admin
from tgbot.handlers.echo import register_echo
from tgbot.handlers.group_approval import register_group_approval
from tgbot.handlers.info_user import register_info_user
from tgbot.handlers.task_3_1_handler import register_show_menu_task_3_1
# from tgbot.handlers.menu import register_menu
# from tgbot.handlers.catch_media import register_catch_media
from tgbot.handlers.task_3_handler import register_show_menu_task_3
from tgbot.handlers.testing import register_testing
from tgbot.handlers.user import register_user
from tgbot.infrastucture.database.functions.setup import create_session_pool
from tgbot.middlewares.acl import ACLMiddleware
from tgbot.middlewares.database import DatabaseMiddleware
from tgbot.middlewares.environment import EnvironmentMiddleware
# from tgbot.middlewares.restriction import RestrictionMiddleware
from tgbot.middlewares.sentinel import Sentinel
from tgbot.middlewares.thottling import ThrotlingMiddleware
from tgbot.notify_admins import on_startup_notify
from tgbot.services.broadcaster import broadcast
# from tgbot.services.init_bot_admins import assign_admin_roles
from tgbot.services.setting_commands import set_default_commands

logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config, session_pool):
    dp.setup_middleware(EnvironmentMiddleware(config=config))
    dp.setup_middleware(DatabaseMiddleware(session_pool=session_pool))
    # dp.setup_middleware(RestrictionMiddleware())
    dp.setup_middleware(ACLMiddleware())
    # dp.setup_middleware(BigBrother())
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
    register_group_approval(dp)
    # register_menu(dp)
    # register_catch_media(dp)
    register_show_menu_task_3(dp)
    register_show_menu_task_3_1(dp)

    register_echo(dp)


async def on_startup(session_pool, bot: Bot, config: Config):
    logger.info("Bot started")
    session: AsyncSession = session_pool()

    # Here we create users in DB and assign them admin roles
    # await assign_admin_roles(session, bot, config.tg_bot.admin_ids)
    await broadcast(bot, config.tg_bot.admin_ids, "Bot started")
    # commands = await get_menu_commands(session)
    # await set_default_commands(bot, commands)
    await session.close()


async def set_all_default_commands(bot):
    # await force_reset_all_commands(bot)
    await set_default_commands(bot)


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
    logger.info("Подключились к БД")
    session_pool = create_session_pool(config.db)

    register_all_middlewares(dp, config, session_pool)
    register_all_filters(dp)
    register_all_handlers(dp)

    await set_all_default_commands(bot)

    # start
    try:
        await on_startup_notify(dp)
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
