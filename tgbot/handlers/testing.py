from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from tgbot.misc.states import Test


async def testing(message: types.Message):
    await message.answer("Вопрос №1\n"
                         "Есть ли жизнь на Марсе?")
    await Test.Q1.set()


async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    # async with state.proxy() as data:
    #     data["answer1"] = answer
    await state.update_data(answer1=answer)
    await message.answer("Вопрос №2\n"
                         "Хочешь полететь на Марс?")
    await Test.Q2.set()


async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = message.text
    await message.answer('Спасибо за ответы')
    await message.answer(f"ответ 1: {answer1}")
    await message.answer(f"ответ 2: {answer2}")
    await state.finish()


def register_testing(dp: Dispatcher):
    dp.register_message_handler(testing, Command("test"))
    dp.register_message_handler(answer_q1, state=Test.Q1)
    dp.register_message_handler(answer_q2, state=Test.Q2)
