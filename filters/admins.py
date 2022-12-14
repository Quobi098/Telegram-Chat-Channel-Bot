from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    async def check(self, m: types.Message) -> bool:
        member = await m.chat.get_member(m.from_user.id)
        return member.is_chat_admin()