from aiogram import types

requestContact = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            types.KeyboardButton(
                text="📞 Telefon raqamini jo'natish",
                request_contact=True
            )
        ]
    ]
)

mainButton = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            types.KeyboardButton(
                text="Ingliz tili"
            ),
            types.KeyboardButton(
                text="Matematika"
            )
        ]
    ]
)
