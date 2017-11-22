#!/usr/bin/python3

import sys
import config
import telebot
import Adafruit_DHT as dht
import time
import os

bot = telebot.TeleBot(config.token)
bot.send_message(config.chadId, 'Hello!!!')

#@bot.message_handler(content_types=["text"])
#def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
#    bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=['temp'])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    build = ''
    try:
        command,build = message.text.split()
    except Exception as ex:
        pass
    if build.lower() in [config.idBuilding]:
        h,t = dht.read_retry(dht.DHT22, 4)
        time.sleep(2)
        h,t = dht.read_retry(dht.DHT22, 4)
        #print 'temp:\t\t{0:0.1f}\nhumidity:\t{1:0.1f}'.format(t, h)
        #print 'temp on proc:\t'; os.system("/opt/vc/bin/vcgencmd measure_temp")
        response = 'temp:\t\t{0:0.1f}\nhumidity:\t{1:0.1f}'.format(t, h)
        response += ' ' + str(message.chat.id)
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "не тот идентификатор")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    h,t = dht.read_retry(dht.DHT22, 4)
    time.sleep(2)
    h,t = dht.read_retry(dht.DHT22, 4)
    #print 'temp:\t\t{0:0.1f}\nhumidity:\t{1:0.1f}'.format(t, h)
    #print 'temp on proc:\t'; os.system("/opt/vc/bin/vcgencmd measure_temp")
    response = 'temp:\t\t{0:0.1f}\nhumidity:\t{1:0.1f}'.format(t, h)
    bot.send_message(message.chat.id, response)

if __name__ == '__main__':
    bot.polling(none_stop=True)

