from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random
import os
import datetime
 
api_id =  
api_hash = ''
app = Client("my_account", api_id=api_id, api_hash=api_hash)

def gettime():
    date = datetime.datetime.now()
    d = date.strftime("%d")
    m = date.strftime("%m")
    t = date.strftime("%X")
    fin = (f'{d}-{m}--{t}')
    return fin

# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)
 
    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")

@app.on_message() 
def message(b, message): 
    # print(message) 
    # print(message.text)
    try:
        if str(message.chat.title) != 'None':
            try:
                file = open(f"C://mav/{message.chat.title}/msgs.txt", "a")
                file.write(f'\n {message.text}')
                file.close()
                print(f'{message.chat.title} | {message.text}')
            except Exception as e:
                file = open(f"C://mav/{message.chat.id}/msgs.txt", "a")
                file.write(f'\n {message.text}')
                file.close()
                print(f'{message.chat.title} | {message.text}')
        else:
            try:
                file = open(f"C://mav/{message.chat.first_name} {message.chat.last_name}/msgs.txt", "a")
                file.write(f'\n {message.text}')
                file.close()
                print(f'{message.chat.first_name} {message.chat.last_name} | {message.text}')

            except OSError:
                file = open(f"C://mav/{message.chat.id}/msgs.txt", "a")
                file.write(f'\n {message.text}')
                file.close()
                print(f'{message.chat.first_name} {message.chat.last_name} | {message.text}')

            except UnicodeEncodeError:
                file = open(f"C://mav/{message.chat.id}/msgs.txt", "a")
                file.write(f'\n Не удалось записать сообщение')
                file.close()

    except FileNotFoundError:
        try:
            os.mkdir(f'C://mav/{message.chat.title}')
            file = open(f"C://mav/{message.chat.title}/msgs.txt", "a")
            file.write(f'\n {message.text}')
            file.close()
            print(f'{message.chat.title} | {message.text}')
        except OSError:
            try:
                os.mkdir(f'C://mav/{message.chat.first_name} {message.chat.last_name}')
                file = open(f"C://mav/{message.chat.first_name} {message.chat.last_name}/msgs.txt", "a")
                file.write(f'\n {message.text}')
                file.close()
                print(f'{message.chat.first_name} {message.chat.last_name} | {message.text}')
            except:
                os.mkdir(f'C://mav/{message.chat.id}')
                file = open(f"C://mav/{message.chat.id}/msgs.txt", "a")
                file.write(f'\n {message.text}')
                file.close()
                print(f'{message.chat.id} | {message.text}')

        except UnicodeEncodeError:
            os.mkdir(f'C://mav/{message.chat.id}')
            file = open(f"C://mav/{message.chat.id}/msgs.txt", "a")
            file.write(f'\n Не удалось записать сообщение')
            file.close()
    try:
        if message.photo.date != 0:
            try:
                if str(message.chat.title) != 'None': 
                    app.download_media(message, f'/mav/{message.chat.title}/') 
                else: 
                    app.download_media(message, f'/mav/{message.chat.first_name} {message.chat.last_name}/') 
            except OSError:
                app.download_media(message, f'/mav/{message.chat.id}/') 
    except AttributeError:
        pass
app.run()
