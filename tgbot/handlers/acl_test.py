from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command

from tgbot.misc.sentinel import allow_access
from tgbot.models.models import User


@allow_access()
async def block_me(message: types.Message, user: User):
    await message.answer(f'Пользователь имеет статус: {user.allowed}. Теперь доступ запрещен. \n'
                         f'Разблокировать можно по команде /unblock_me')
    user.block()


@allow_access()
async def unblock_me(message: types.Message, user: User):
    await message.answer(f'Пользователь имеет статус: {user.allowed}. Теперь доступ разрешен. \n'
                         f'заблокировать можно по команде /block_me')
    user.allow()


def register_acl_test(dp: Dispatcher):
    dp.register_message_handler(block_me, Command('block_me'))
    dp.register_message_handler(unblock_me, Command('unblock_me'))
