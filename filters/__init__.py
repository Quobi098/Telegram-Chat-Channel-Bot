from aiogram import Dispatcher
from .private_chat import IsPrivate
from .admins import AdminFilter
from .group_chat import IsGroup

def setup(dp: Dispatcher):
    pass
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
