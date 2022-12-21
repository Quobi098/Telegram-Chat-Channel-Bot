from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import allowed_users
from loader import dp

@dp.inline_handler(text="")
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Введите какой-то запрос",
                input_message_content=types.InputTextMessageContent(
                    message_text="Не оязательно жать при этом на кнопку",
                )
            )
        ],
        cache_time=5
    )


@dp.inline_handler()
async def some_query(query: types.InlineQuery):
    user = query.from_user.id
    if user not in allowed_users:
        await query.answer(
            results=[],
            switch_pm_text="Бот недоступен. Подключить бота",
            switch_pm_parameter="connect_user",
            cache_time=5
        )
        return

    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="Название, которое отображается в инлайн режиме!",
                input_message_content=types.InputTextMessageContent(
                    message_text="Тут какой-то <b>текст</b>, который будет отправлен при нажатии на кнопку"
                ),
                url="https://core.telegram.org/api/bots/inline",
                thumb_url="https://core.telegram.org/api/bots/inline",
                description="Описание в инлайн режиме"
            ),
            types.InlineQueryResultVideo(
                id="4",
                video_url="https://www.youtube.com/watch?v=UMPofnwxgKI&list=PL8Viaihva15kMj4RamorHHLjszhV0qSYg&index=26",
                caption="The Real Slim Shady - Eminem (Lyrics)",
                title="Eminem (Lyrics)",
                description="No description",
                thumb_url="https://i.pinimg.com/originals/a2/78/52/a27852f3eaea51a4843747763857e232.jpg",
                mime_type="video/mp4"
            )
        ]
    )

@dp.message_handler(CommandStart(deep_link="connect_user"))
async def connect_user(message: types.Message):
    allowed_users.append(message.from_user.id)
    await message.answer("Вы подключены",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text="Войти в инлайн режим",
                                                          switch_inline_query_current_chat="Запрос")
                                 ]
                             ]
                         ))
