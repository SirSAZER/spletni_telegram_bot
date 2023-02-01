from aiogram import Bot, Dispatcher, executor, types
from keyboards import ikb
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Я родился!')


@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message):
    await msg.answer(text='Приветствую тебя, дорогой ученик 301 школы! Ты можешь мне открыться и выдать все свои тайны, конечно, в рамках школы)')
    await bot.send_message(chat_id=msg.from_user.id,
                            text='Как ты хочешь отпрвить <em><b>свою новость</b></em>!',
                            parse_mode='HTML',
                            reply_markup=ikb)


@dp.callback_query_handler()
async def anon_call(clb: types.CallbackQuery):
    if clb.data == 'ANON':
        await clb.answer(text='ВЫ ВЫБРАЛИ ТЕМНУЮ СТОРОНУ СИЛЫ😈')
    elif clb.data == 'PUB':
        return await clb.answer(text='ВЫ ВЫБРАЛИ СВЕТЛУЮ СТОРОНУ СИЛЫ😇')




if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)