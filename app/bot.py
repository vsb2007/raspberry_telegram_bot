#!/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals 
from flask import Flask, request  # Импортируем модули
import telegram

import sys
import Adafruit_DHT as dht
import time
import os

sys.path.append('./config')
import myconfig

app = Flask(__name__) # Создаем приложение
app.debug = True


MY_URL = myconfig.url
TOKEN = myconfig.token
TEMP_COMMAND = myconfig.tempcommand
BUILD = myconfig.idBuilding
CERT = 'fullchain1.pem'

global bot
bot = telegram.Bot(token=TOKEN)

bot.send_message(myconfig.chadId, 'Hello!!!')

def bot_send(bot,chat_id,message):
    i=0
    try:
	bot.send_message(chat_id=chat_id, text=message)
	print ("сообщение ушло").encode('utf8')
    except Exception, e:
	print ("не удачно отослали, ошибка ниже:").encode('utf8')
	print(e)
	print ("еще раз:").encode('utf8')
	try:
	    bot.send_message(chat_id=chat_id, text=message)
	    print ("сообщение ушло").encode('utf8')
	except Exception, e2:
	    print ("2й раз тоже не получилось:").encode('utf8')
	    print(e2)
	    print("выходим").encode('utf8')
    return "ok"

def send_command(chat_id,command):
    if command.lower() in [TEMP_COMMAND]:
	try:
	    h,t = dht.read_retry(dht.DHT22, 4)
    	    time.sleep(2)
    	    h,t = dht.read_retry(dht.DHT22, 4)
        #print 'temp:\t\t{0:0.1f}\nhumidity:\t{1:0.1f}'.format(t, h)
        #print 'temp on proc:\t'; os.system("/opt/vc/bin/vcgencmd measure_temp")
    	    response = 'temp:\t\t{0:0.1f}\nhumidity:\t{1:0.1f}'.format(t, h)
    	#response += ' ' + str(chat_id)
	    bot_send(bot,chat_id,response)
	except Exception, e2:
    	    bot_send(bot,chat_id,"нет доступа к gpio")
    else:
	bot_send(bot,chat_id,"не тa команда")

#WebHook
@app.route('/hook%s' % TOKEN, methods=['POST', 'GET'])
def webhook_handler():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        try:
            chat_id = update.message.chat.id
            text = update.message.text
            userid = update.message.from_user.id
            username = update.message.from_user.username
            #bot.send_message(chat_id=chat_id, text="hello")
	    build = ''
	    try:
    		build,command = text.split()
#		print(command)
#		print(build)
	    except Exception as e:
#		try:
#		    command = text
#		    send_command(chat_id,command)
#		    return "ok"
#		except Exception as e2:
#		    bot_send(bot,chat_id,"error: ошибка парсинга")
#		    return "ok"
    		pass
	    if build.lower() not in ['/'+BUILD]:
		#bot_send(bot,chat_id,"указан не существующий бот")
		return "ok"
	    else:
		pass
	    send_command(chat_id,command)
#	    if command.lower() in [TEMP_COMMAND]:
#    		h,t = dht.read_retry(dht.DHT22, 4)
#    		time.sleep(2)
#    		h,t = dht.read_retry(dht.DHT22, 4)
#        #print 'temp:\t\t{0:0.1f}\nhumidity:\t{1:0.1f}'.format(t, h)
#        #print 'temp on proc:\t'; os.system("/opt/vc/bin/vcgencmd measure_temp")
#    		response = 'temp:\t\t{0:0.1f}\nhumidity:\t{1:0.1f}'.format(t, h)
#    		response += ' ' + str(chat_id)
#		bot_send(bot,chat_id,response)
#	    else:
#		bot_send(bot,chat_id,"не тa команда")

	    #print(bot.getWebhookInfo())
        except Exception, e:
            print e
    return 'ok'


##Set_webhook 
#hookurl = "https://%s/hook%s" % (MY_URL,TOKEN)
#allowed_updates = ["message", "callback_query"]
#max_connections = 40
#URL = "https://api.telegram.org/bot%s/" % TOKEN
#CERT = "fullchain1.pem"

#@app.route('/set_webhook', methods=['GET', 'POST']) 
#def set_webhook():
#    s = bot.deleteWebhook()
#    s = bot.setWebhook(
#	hookurl
##	, certificate=open(CERT, 'r') # используется для самоподписных сертификатов
#	, max_connections=max_connections
#	, allowed_updates=allowed_updates
#    )
#    print(bot.getWebhookInfo())
#    if s:
#        print(s)
#	print(bot.getWebhookInfo())
#        return "webhook setup ok" 
#    else: 
#        return "webhook setup failed" 
#
#@app.route('/del_webhook', methods=['GET', 'POST']) 
#def del_webhook(): 
#    s = bot.deleteWebhook()
#    print(bot.getWebhookInfo())
#    if s:
#        print(s)
#	print(bot.getWebhookInfo())
#	#print(bot.getUpdates())
#        return "webhook delete ok" 
#    else: 
#        return "webhook delete failed" 
#
@app.route('/') 
def index(): 
    return '<h1>Hello</h1>'
