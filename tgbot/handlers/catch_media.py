from aiogram import types, Dispatcher


async def catch_text(message: types.Message):
    await message.answer('Вы прислали текст')


async def catch_video(message: types.Message):
    # await message.reply('Вы прислали Video')
    await message.video.download()
    await message.reply("Видео скачано\n"
                        f"<pre>FILE ID = {message.document.file_id}</pre>",
                        parse_mode="HTML")


async def catch_photo(message: types.Message):
    await message.reply('Вы прислали Photo')
    await message.photo[-1].download()
    await message.reply("Фото скачано\n"
                        f"<pre>FILE ID = {message.photo[-1].file_id}</pre>",
                        parse_mode="HTML")


async def catch_doc(message: types.Message):
    await message.answer('Вы прислали текст')


def register_catch_media(dp: Dispatcher):
    dp.register_message_handler(catch_text)
    dp.register_message_handler(catch_video, content_types=types.ContentTypes.VIDEO)
    dp.register_message_handler(catch_photo, content_types=types.ContentTypes.PHOTO)
    dp.register_message_handler(catch_doc, content_types=types.ContentTypes.DOCUMENT)