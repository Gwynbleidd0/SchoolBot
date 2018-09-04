import botT
import config
import telebot
from telebot import apihelper
from telebot import types

apihelper.proxy = {'https':'https://77.252.133.48:25772'}
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["get"])
def get_raspisanie(message):
    bot.send_message(message.chat.id,botT.get_timetable())
@bot.message_handler(commands=["start"])
def random_messages(message):
    bot.send_message(message.chat.id,"Это первая версия бота для 11А")
if __name__ == '__main__':
		bot.polling(none_stop=True)
    
