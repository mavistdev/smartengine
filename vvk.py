import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import json
import socket
from win10toast import ToastNotifier

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
vk_session = vk_api.VkApi(token='')
longpoll = VkBotLongPoll(vk_session, '213378612')
toaster = ToastNotifier()

def connecttoserver(ip, port):
    try:
        client.connect((ip, port))
        client.send('[VK-MESSAGE-GRABBER] '.encode('utf-8'))
    except:
        print('Подключение не удалось. Сервер недоступен.')

connecttoserver("127.0.0.1", 12345)
client.send(' connected'.encode('utf-8'))

def getid(uid):
    user = vk_session.method("users.get", {"user_ids": uid})
    fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']
    return(fullname)

def main():
    """ Пример использования bots longpoll
        https://vk.com/dev/bots_longpoll
    """
    vk_session = vk_api.VkApi(token='')
    longpoll = VkBotLongPoll(vk_session, '213378612')
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            uid = event.obj["message"]["from_id"]
            user = vk_session.method("users.get", {"user_ids": uid})
            fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']
            print('Новое сообщение:')
            print(f'Для меня от: {fullname}', end=' ')
            print()
            print('Текст: ', event.obj["message"]["text"])
            print()
            toaster.show_toast(
                fullname,
                event.obj["message"]["text"],
                duration=3,
                threaded=True)
            try:
              if event.obj["message"]["reply_message"] != '':
                aaaa = {event.obj["message"]["reply_message"]["from_id"]}
                try:
                  repl_from = getid(aaaa)
                except:
                  repl_from = '0'
                print(f'Ответ на "{event.obj["message"]["reply_message"]["text"]}" от {repl_from}')
            except:
              print('no repl')
              print()

        # elif event.type == VkBotEventType.MESSAGE_REPLY:
        #     # print('Новое сообщение:')
        #     # print('От меня для: ', end='')
        #     # print(event.obj.peer_id)
        #     # print('Текст:', event.obj.text)
        #     print()
        #     print(event.obj[message])
        elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            print('Печатает ', end='')
            user = vk_session.method("users.get", {"user_ids": event.obj.from_id})
            fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']
            print(fullname, end=' ')
            print('для ', end='')
            print(event.obj.to_id)
            print()

        elif event.type == VkBotEventType.GROUP_JOIN:
            print(event.obj.user_id, end=' ')
            print('Вступил в группу!')
            print()

        elif event.type == VkBotEventType.GROUP_LEAVE:
            print(event.obj.user_id, end=' ')
            print('Покинул группу!')
            print()
        # else:
        #     print(event.type)
        #     print()

if __name__ == '__main__':
    client.send('[VK-MESSAGE-GRABBER] connected'.encode('utf-8'))
    main()


