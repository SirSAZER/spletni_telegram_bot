from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb = InlineKeyboardMarkup(row_width=2,inline_keyboard=True)
ib1 = InlineKeyboardButton(text='Анонимно', callback_data='ANON')
ib2 = InlineKeyboardButton(text='Публично', callback_data='PUB')
ikb.add(ib1, ib2)



