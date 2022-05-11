import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile

from config import config
from keyboards import markups as kb
from data import data_op as op, data_text as te

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    photo = InputFile("0.png")
    await bot.send_photo(chat_id=message.from_user.id,photo=photo,caption=te.START,reply_markup=kb.play)
    await bot.delete_message(message.from_user.id, message.message_id)

@dp.callback_query_handler(text='play')
async def about(msg: types.Message):
    await bot.send_message(msg.from_user.id,te.DISCLEIM,reply_markup=kb.OK)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='next_round')
async def about(msg: types.Message):
    r = random.randint(1,29)
    photo = InputFile("pictures/"+str(r)+".png")
    await bot.send_photo(chat_id=msg.from_user.id, photo=photo,caption=op.data_op[r],reply_markup=kb.main)

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_other_messages(message: types.Message):
    await message.answer("Я не совсем понимаю тебя .Введите /start", reply_markup=kb.back)
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.delete_message(message.from_user.id, message.message_id - 1)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
