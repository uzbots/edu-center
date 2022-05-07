from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from filters import IsPrivate


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    matn = f"<b>Assalom alaykum hurmatli {message.from_user.full_name}!</b>\n"
    matn += "Sizni <b>EDU-Center</b> akademyasini rasmiy Telegram botida ko'rib turganimdan hursandman.\n"
    matn += "Marhamat ro'yhatdan o'tish uchun /register buyrug'ini kiriting..."
    await message.answer(text=matn)
