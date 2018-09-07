

from django import forms
from .models import *

class Attendance_Form(forms.Form):
    name=forms.CharField(max_length=20,label='名前')
    password=forms.CharField(min_length=5,max_length=15,widget=forms.PasswordInput,label='パスワード')

