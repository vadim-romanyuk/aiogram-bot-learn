from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command

from tgbot.keyboards.menu_kb import menu


async def show_menu(message: types.Message):
    await message.answer('Выберите товар', reply_markup=menu)


async def get_text_button(message: types.Message):
    await message.answer('Вы выбрали котлетки')


def register_menu(dp: Dispatcher):
    dp.register_message_handler(show_menu, Command('menu'))
    dp.register_message_handler(get_text_button, text='макароны')



