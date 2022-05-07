from aiogram import Dispatcher

from loader import dp
from .is_admin import IsAdmin
from .is_private import IsPrivate
from .is_group import IsGroup


if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsGroup)
