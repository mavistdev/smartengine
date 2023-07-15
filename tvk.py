import telebot
import requests
bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	print(message.text)
	requests.post('', {"content": message.text})

bot.polling(none_stop=True, interval=0)
