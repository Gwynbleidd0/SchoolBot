import botT
import config
import telebot
import fille
from SQLighter import SQLighter
from telebot import apihelper
from telebot import types

"""def search_fille():
    lis = botT.get_timetable()
    print(lis[0])
    print(lis[1])
    if lis[0]==True:
        fille = lis[1]
    else:
        fille = botT.get_lastfille()
    return(fille)
"""
db_worker=SQLighter('DB.db')
apihelper.proxy = {'https':'https://96.252.117.163:31864'}
bot = telebot.TeleBot(config.token)
markup_start = types.ReplyKeyboardMarkup()
markup_start.row('11а','11б','11в')
markup_start.row('Инфо, так сказать')

date = ''
date_real = ''




@bot.message_handler(commands=["/start"])
def random_messages(message):
    db_worker.add_user_inf(message.from_user.username)
    bot.send_message(message.chat.id,"Этот бот был создан для получения расписания.Проблемы?",reply_markup=markup_start)
@bot.message_handler(content_types=["text"])
def get_raspisanie(message):
    global date
    global date_real
    if message.text=='11а':
#        date_real=fille.get_date()
#        if date_real != date:
#            reslist = botT.get_timetable2()
#            date=reslist[1]
        botT.get_timetable2()
        alfa = botT.get_book('11а')
        bot.send_message(message.chat.id,alfa,reply_markup=markup_start)
    if message.text=='11б':
#        date_real=fille.get_date()
#        if date_real != date:
#            reslist = botT.get_timetable2()
#            date=reslist[1]
        botT.get_timetable2()
        alfa = botT.get_book('11б')
        bot.send_message(message.chat.id,alfa,reply_markup=markup_start)
    if message.text=='11в':
        date_real=fille.get_date()
        if date_real != date:
            reslist = botT.get_timetable2()
            date=reslist[1]
        alfa = botT.get_book('11в')
        bot.send_message(message.chat.id,alfa,reply_markup=markup_start)
    if message.text=='Инфо, так сказать':
        bot.send_message(message.chat.id,'v1.4\nВсе права принадлежат тому, кому принадлежат.\nЧто пишет на доске гуманитарий, когда его вызывают на задачу по физике?\n Не дано',reply_markup=markup_start)

if __name__ == '__main__':
		bot.polling(none_stop=True)
    

