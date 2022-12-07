from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command

from tgbot.keyboards.task_3_kb import task_3_kb_in


async def show_menu_task_3(message: types.Message):
    await message.answer('Edit @Sberleadbot info.\n'
                         'Name: Бот для Заданий на Курсе Udemy\n'
                         'Description: ?\n'
                         'About: ?\n'
                         'Botpic: ? no botpic\n'
                         'Commands: no commands yet\n', reply_markup=task_3_kb_in)


def register_show_menu_task_3(dp: Dispatcher):
    dp.register_message_handler(show_menu_task_3, Command('inline_buttons_1'))
