import telebot
import requests
bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	print(message.text)
	requests.post('https://discord.com/api/webhooks/1064086850823798804/wbErnY1izmxVKGI6tg9R4MEO22vPtTb1Jn1yuXGve6f8097pdwRElrBK6uMmsd22lg01', {"content": message.text})

bot.polling(none_stop=True, interval=0)
