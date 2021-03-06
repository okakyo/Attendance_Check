from django.shortcuts import render
from django.views.generic import View
from .models import Attendance_Model
from .forms import Attendance_Form
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.
import datetime
from .arrangement import write_time,spread_sheet

def Write(style='CSV',*args,**kwargs):
    if style=='CSV':
        write_time(*args,**kwargs)
    elif style=='google':
        spread_sheet(*args,**kwargs)
    else:
        raise ValueError

class index(View):

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
            user = User.objects.get(username=user)
            model=Attendance_Model.objects.filter(name=user,date=datetime.date.today().strftime('%Y-%m-%d'))

            if not model.exists():
                model=Attendance_Model(name=user)
                write_time(datetime.date.today(), user, datetime.datetime.now().strftime('%H:%M:%S'), '出勤')
                self.param['message'] = '{}の出勤を確認しました。'.format(user)

            else:
                model=model.get(name=user,date=datetime.date.today().strftime('%Y-%m-%d'))

                if model.arrival%2==0:
                    write_time(datetime.date.today(), user, datetime.datetime.now().strftime('%H:%M:%S'), '出勤')
                    self.param['message'] = '{}の出勤を確認しました。'.format(user)

                else:
                    write_time(datetime.date.today(), user, datetime.datetime.now().strftime('%H:%M:%S'), '退勤')
                    self.param['message'] = '{}の退勤を確認しました。お疲れさまでした'.format(user)
            model.arrival +=1
            model.save()

        return render(request, 'index.html', self.param)