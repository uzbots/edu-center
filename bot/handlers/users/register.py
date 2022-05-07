from aiogram import types

from loader import dp
from keyboards.default import requestContact
from filters import IsPrivate
from states import Register


@dp.message_handler(IsPrivate(), commands=['register'])
async def register(message: types.Message):
    matn = "<b>1/4: Ro'yhatdan o'tish boshlandi...</b>\n"
    matn += "<b>Raqam jo'nating</b>\n\n"
    matn += "<i>Ro'yhatdan o'tishni bekor qilish ucgun /cancel buyrug'ini kiriting...</i>"
    await message.answer(text=matn, reply_markup=requestContact)
    await Register.phoneNumber.set()
