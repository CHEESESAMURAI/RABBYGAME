from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

play = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='Let’s play',callback_data='play')
play.insert(btn1)

OK = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='OK',callback_data='next_round')
OK.insert(btn1)

main = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='😈😈😈',url='https://www.wildberries.ru/brands/freeedom')
btn2 = InlineKeyboardButton(text='❤Давай еще❤',callback_data='next_round')
main.insert(btn1)
main.insert(btn2)