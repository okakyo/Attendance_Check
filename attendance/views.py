from django.shortcuts import render
from django.views.generic import FormView
from .models import Attendance_Model
from .forms import Attendance_Form
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.
import datetime
import time,os
from .arrangement import write_time
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import  MessageEvent, TextMessage, TextSendMessage,FollowEvent

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@handler.add(MessageEvent)
def answer_check(event,name,check):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='{}さんの{}を確認しました。'.format(name,check)))


class index(FormView):
    template_name = 'index.html'
    success_url = '/'

    def __init__(self):
        self.today = datetime.datetime.today()
        super().__init__()

        self.param = {

            'message': 'フォームに名前、パスワードを入力してください。',
            'form': Attendance_Form,
            'model': Attendance_Model.objects.filter(date=datetime.date.today().strftime('%Y-%m-%d'))
        }

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', self.param)

    def post(self, request, *args, **kwargs):
        user = request.POST['name']
        password = request.POST['password']
        check = authenticate(request, username=user, password=password)

        if check is None:
            self.param['message'] = 'ユーザー名、またはパスワードが違います。ご確認ください。'
        else:
            
            #LINEで通知させたほうがいい。
            if not self.param['model'].values('arrival'):
                user = User.objects.get(username=user)
                model = Attendance_Model(name=user, arrival=True)
                write_time(datetime.date.today(), user, datetime.datetime.now().strftime('%H:%M:%S'), '出勤')
                model.save()
                answer_check(event,name=user,check='出勤')
                self.param['message'] = '{}の出勤を確認しました。'.format(user)
            
            else:
                user = User.objects.get(username=user)
                model = Attendance_Model(name=user, arrival=False)
                write_time(datetime.date.today(), user, datetime.datetime.now().strftime('%H:%M:%S'), '退勤')
                model.save()
                answer_check(event,name=user,check='退勤')
                self.param['message'] = '{}の退勤を確認しました。お疲れさまでした'.format(user)

        return render(request, 'index.html', self.param)