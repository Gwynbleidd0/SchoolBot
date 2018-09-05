import botT
import config
import telebot
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

apihelper.proxy = {'https':'https://195.77.247.139:50591'}
bot = telebot.TeleBot(config.token)
markup_start = types.ReplyKeyboardMarkup()
markup_start.row('Получить расписание')
markup_start.row('Инфо, так сказать')
last_fille='5 сентября. 1 смена.xls'
@bot.message_handler(commands=["start"])
def random_messages(message):
    bot.send_message(message.chat.id,"Это первая версия бота для 11А",reply_markup=markup_start)
@bot.message_handler(content_types=["text"])
def get_raspisanie(message):
    if message.text=='Получить расписание':
        search_fille()
        alfa = botT.get_book(search_fille())
        bot.send_message(message.chat.id,alfa,reply_markup=markup_start)
    if message.text=='Инфо, так сказать':
        bot.send_message(message.chat.id,'v1.3\nВсе права принадлежат тому, кому принадлежат.\nВидеоблог скоро!',reply_markup=markup_start)

if __name__ == '__main__':
		bot.polling(none_stop=True)
    

