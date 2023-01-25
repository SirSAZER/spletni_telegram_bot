from aiogram import Bot, Dispatcher, executor, types
from keyboards import ikb, kb
from config import TOKEN



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Я родился!')


@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message):
    await msg.answer(text='Welcome!',
                    reply_markup=kb)


@dp.message_handler(commands=['links'])
async def links_command(msg: types.Message):
    await msg.answer(text='Chosee options!',
                    reply_markup=ikb)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)