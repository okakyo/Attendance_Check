from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime

class Attendance_Model(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    arrival=models.IntegerField(default=0)
    date=models.DateField(default=datetime.datetime.today().strftime('%Y-%m-%d'))
    check_time=models.TimeField(default=datetime.datetime.now().strftime('%H:%M:%S'))

    def __str__(self):
        return str(self.name)

class Password_model(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    password=models.CharField(max_length=50)


