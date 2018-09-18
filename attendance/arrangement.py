import pandas as pd
import csv,os
import datetime
import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import  MessageEvent, TextMessage, TextSendMessage,FollowEvent

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

def write_time(date,name,time,check):
    with open('calculator.csv','a',encoding='UTF-8') as w:
        writer=csv.writer(w)
        writer.writerow([date,name,time,check])


@handler.add(MessageEvent)
def answer_check(event,name,check):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='{}さんの{}を確認しました。'.format(name,check)))



    

