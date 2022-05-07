from aiogram import types
from aiogram.dispatcher.dispatcher import FSMContext

from loader import dp
from filters import IsPrivate


@dp.message_handler(IsPrivate(), commands=['cancel'], state='*')
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Ro'yhatdan o'tishni bekor qilindi!")
