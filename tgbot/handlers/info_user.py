from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from tgbot.misc.states import UserInfo


async def user_info(message: types.Message):
    await message.answer("Введи Имя")
    await UserInfo.Name.set()


async def answer_name(message: types.Message, state: FSMContext):
    answer = message.text
    # async with state.proxy() as data:
    #     data["answer1"] = answer
    await state.update_data(answer1=answer)
    await message.answer("Введи email")
    await UserInfo.Email.set()


async def answer_email(message: types.Message, state: FSMContext):
    answer = message.text
    # async with state.proxy() as data:
    #     data["answer1"] = answer
    await state.update_data(answer2=answer)
    await message.answer("Введи телефон")
    await UserInfo.Phone.set()


async def answer_phone(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = data.get('answer2')
    answer3 = message.text
    await message.answer(f'Привет! Ты ввел следующие данные:\n'
                         f'Имя: {answer1}\n'
                         f'Email: {answer2}\n'
                         f'Телефон: {answer3}')
    # await state.finish()
    await state.reset_state(with_data=True)


def register_info_user(dp: Dispatcher):
    dp.register_message_handler(user_info, Command("form"))
    dp.register_message_handler(answer_name, state=UserInfo.Name)
    dp.register_message_handler(answer_email, state=UserInfo.Email)
    dp.register_message_handler(answer_phone, state=UserInfo.Phone)
