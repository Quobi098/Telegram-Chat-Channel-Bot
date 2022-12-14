from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку',
        '/menu - Работа с ботом',
        '/set_photo - Установить фото в группе',
        '/set_title - Установить название группы',
        '/set_description - Установить описание группы',
        '/ro - Режим Read Only',
        '/unro - Отключить RO',
        '/ban - Забанить',
        '/unban - Разбанить'
    ]
    await message.answer('\n'.join(text))
