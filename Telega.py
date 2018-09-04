import botT
import config
import telebot
from telebot import apihelper
from telebot import types

#apihelper.proxy = {'https':'https://109.104.144.46:80'}
bot = telebot.TeleBot(config.token)
markup_start = types.ReplyKeyboardMarkup()
markup_start.row('Получить расписание')
markup_start.row('Инфо, так сказать')
@bot.message_handler(commands=["start"])
def random_messages(message):
    bot.send_message(message.chat.id,"Это первая версия бота для 11А",reply_markup=markup_start)
@bot.message_handler(content_types=["text"])
def get_raspisanie(message):
    if message.text=='Получить расписание':
        bot.send_message(message.chat.id,botT.get_timetable(),reply_markup=markup_start)
    if message.text=='Инфо, так сказать':
        bot.send_message(message.chat.id,'v1.2\nВсе права принадлежат тому, кому принадлежат.\nБ класс пидоры. Аминь',reply_markup=markup_start)

if __name__ == '__main__':
		bot.polling(none_stop=True)
    
