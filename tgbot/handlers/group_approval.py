import random


from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.callback_data import CallbackData

approval_cb = CallbackData('chat_join_request', 'approve', 'chat_id')


async def process_chat_invite_request(chat_join_request: ChatJoinRequest, state: FSMContext):
    approve_buttons = [
        InlineKeyboardButton(text='🐈',
                             callback_data=approval_cb.new(approve='1', chat_id=chat_join_request.chat.id)),
        InlineKeyboardButton(text='🐶',
                             callback_data=approval_cb.new(approve='0', chat_id=chat_join_request.chat.id)),
        InlineKeyboardButton(text='🐬',
                             callback_data=approval_cb.new(approve='0', chat_id=chat_join_request.chat.id))

    ]
    random.shuffle(approve_buttons)
    await chat_join_request.bot.send_message(
        chat_join_request.from_user.id,
        'Нажмите на котика',
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[approve_buttons])
    )


async def approve_callback_group_captcha(call: CallbackQuery, callback_data: dict):
    await call.message.delete_reply_markup()
    chat_id = callback_data['chat_id']
    await call.bot.approve_chat_join_request(chat_id, call.from_user.id)


async def decline_callback_group_captcha(call: CallbackQuery, callback_data: dict):
    await call.message.delete_reply_markup()
    await call.message.answer('вы не приняты')
    chat_id = callback_data['chat_id']
    await call.bot.decline_chat_join_request(chat_id, call.from_user.id)


def register_group_approval(dp: Dispatcher):
    dp.register_chat_join_request_handler(process_chat_invite_request, )
    dp.register_callback_query_handler(approve_callback_group_captcha, approval_cb.filter(approve='1'))
    dp.register_callback_query_handler(decline_callback_group_captcha, approval_cb.filter())

