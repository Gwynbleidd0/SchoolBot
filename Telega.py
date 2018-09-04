import botT
import config
import telebot
from telebot import apihelper
from telebot import types

#apihelper.proxy = {'https':'https://77.252.133.48:25772'}
bot = telebot.TeleBot(config.token)
markup_start = types.ReplyKeyboardMarkup()
markup_start.row('Получить расписание')
markup_start.row('Инфо, так сказать')
@bot.message_handler(content_types=["text"])
def get_raspisanie(message):
    if message.text=='Получить расписание':
        bot.send_message(message.chat.id,botT.get_timetable())
    if message.text=='Инфо, так сказать':
        bot.send_message(message.chat.id,'v1.2 Все права принадлежат тому, кому принадлежат. Б класс пидоры. Аминь')
@bot.message_handler(commands=["start"])
def random_messages(message):
    bot.send_message(message.chat.id,"Это первая версия бота для 11А")
if __name__ == '__main__':
		bot.polling(none_stop=True)
    
