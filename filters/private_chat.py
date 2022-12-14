from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import dp

class IsPrivate(BoundFilter):

    async def check(self, message:types.Message):
        return message.chat.type == types.ChatType.PRIVATE