from aiogram import types
from aiogram.dispatcher.dispatcher import FSMContext

from loader import dp, bot
from data.config import ADMINS
from keyboards.default import mainButton, tasdiqlashBtn
from states import Register
from filters import IsPrivate


@dp.message_handler(IsPrivate(), state=Register.phoneNumber, content_types=types.ContentTypes.CONTACT)
async def register_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(
        {"phone_number": message.contact.phone_number}
    )
    matn = f"<b>2/4: {message.contact.phone_number} - raqam qabul qilindi.</b>\n"
    matn += "<b>Ism va familiya kiriting...</b>"
    await message.answer(text=matn, reply_markup=types.ReplyKeyboardRemove())
    await Register.fullName.set()


@dp.message_handler(IsPrivate(), state=Register.fullName, content_types=types.ContentTypes.TEXT)
async def register_full_name(message: types.Message, state: FSMContext):
    await state.update_data(
        {'full_name': message.text}
    )
    matn = f"<b>3/4: {message.text} - ism va familiya qabul qilindi.</b>\n"
    matn += "<b>Siz ta'lim olmoqchi bo'lgan kursni tanlang...</b>"
    await message.answer(text=matn, reply_markup=mainButton)
    await Register.course.set()


@dp.message_handler(IsPrivate(), state=Register.course, content_types=types.ContentTypes.TEXT)
async def register_course(message: types.Message, state: FSMContext):
    await state.update_data(
        {'course': message.text}
    )
    data = await state.get_data()
    matn = f"<b>4/4: {message.text} - kursi tanlandi</b>\n"
    matn += f"Ism va Familiya: {data.get('full_name')}\n"
    matn += f"Raqam: {data.get('phone_number')}\n"
    matn += f"Kurs: {data.get('course')}\n\n"
    matn += "<b>Malumotlar to'g'rimi?</b>"
    await message.answer(text=matn, reply_markup=tasdiqlashBtn)
    await Register.confirm.set()


@dp.callback_query_handler(state=Register.confirm)
async def register_finish(query: types.CallbackQuery, state: FSMContext):
    callbackData = query.data
    if callbackData == 'yes':
        data = await state.get_data()
        matn = "<b>Yangi foydalanuvchi ariza qoldirdi!</b>\n\n"
        matn += f"Ism: <a href='tg://user?id={query.from_user.id}'>{data.get('full_name')}</a>\n"
        matn += f"Raqam: {data.get('phone_number')}\n"
        matn += f"Kurs: {data.get('course')}"
        await bot.send_message(chat_id=ADMINS[0], text=matn)
        await bot.send_message(chat_id=query.from_user.id, text="<b>Malumotlar qabul qilindi, operatorlarimiz yaqin fursatlarda sizga bog'lanishadi!</b>")
        await state.finish()

    elif callbackData == 'no':
        await query.message.answer("<b>Malumotlar o'chirildi, qaytadan boshlash uchun: /register</b>")
        await state.finish()

    else:
        await state.finish()
