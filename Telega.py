import botT
import config
import telebot
from SQLighter import SQLighter
from telebot import apihelper
from telebot import types

def search_fille():
    lis = botT.get_timetable()
    print(lis[0])
    print(lis[1])
    if lis[0]==True:
        fille = lis[1]
    else:
        fille = botT.get_lastfille()
    return(fille)

db_worker=SQLighter('DB.db')
#apihelper.proxy = {'https':'https://203.153.216.188:31572'}
bot = telebot.TeleBot(config.token)
markup_start = types.ReplyKeyboardMarkup()
markup_start.row('11а','11в')
markup_start.row('Инфо, так сказать')
last_fille='5 сентября. 1 смена.xls'
@bot.message_handler(commands=["start"])
def random_messages(message):
    db_worker.add_user_inf(message.from_user.username)
    bot.send_message(message.chat.id,"Это первая версия бота для 11А",reply_markup=markup_start)
@bot.message_handler(content_types=["text"])
def get_raspisanie(message):
    if message.text=='11а':
        botT.get_timetable()
        alfa = botT.get_book('11а')
        bot.send_message(message.chat.id,alfa,reply_markup=markup_start)
    if message.text=='11в':
        botT.get_timetable()
        alfa = botT.get_book('11в')
        bot.send_message(message.chat.id,alfa,reply_markup=markup_start)
    if message.text=='Инфо, так сказать':
        bot.send_message(message.chat.id,'v1.3\nВсе права принадлежат тому, кому принадлежат.\nАлла заебала!!!',reply_markup=markup_start)

if __name__ == '__main__':
		bot.polling(none_stop=True)
    

