import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile

from config import config
from keyboards import markups as kb
from data import data_op as op, data_text as te

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

file_id = 0
users_id = []
admins_id = []

state = 0

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    global users_id
    photo = InputFile(te.START_PNG)
    await bot.send_photo(chat_id=message.from_user.id,photo=photo,caption=te.START,reply_markup=kb.play)
    await bot.delete_message(message.from_user.id, message.message_id)
    id_us = message.from_user.id
    print(id_us)
    if id_us not in users_id :
        users_id.append(id_us)
    print(users_id)

@dp.message_handler(commands=['setup'])
async def start_cmd(message: types.Message):
    global state
    await bot.send_message(message.from_user.id,te.ENTER_KEY)
    state = 1
    await bot.delete_message(message.from_user.id, message.message_id)

@dp.callback_query_handler(text='play')
async def about(msg: types.Message):
    await bot.send_message(msg.from_user.id,te.DISCLEIM,reply_markup=kb.OK)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.message_handler(content_types=["photo"])
async def get_photo(message):
    global file_id
    global admins_id
    global users_id

    for i in admins_id:
        if message.from_user.id == i:
            file_id = message.photo[-1].file_id
            caption = message.caption
            await bot.delete_message(message.from_user.id, message.message_id)
            for i in users_id:
                try:
                    await bot.send_photo(chat_id=i,photo=file_id,caption=caption)
                except Exception as e:
                    print('сырный тут')
        else:
            await bot.delete_message(message.from_user.id, message.message_id)

@dp.callback_query_handler(text='next_round')
async def about(msg: types.Message):
    r = random.randint(1,29)
    photo = InputFile("pictures/"+str(r)+".png")
    await bot.send_photo(chat_id=msg.from_user.id, photo=photo,caption=op.data_op[r],reply_markup=kb.main)

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_other_messages(message: types.Message):
    global admins_id
    global users_id
    global state

    if state == 1:
        if message.text == te.ADMIN_KEY:
            await bot.send_message(message.from_user.id,te.ACCES)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            if message.from_user.id not in admins_id:
                admins_id.append(message.from_user.id)
                state = 0
        else:
            await bot.send_message(message.from_user.id,te.NOTACCES)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
    else:
        await message.answer("Я не совсем понимаю тебя .Введите /start")
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
