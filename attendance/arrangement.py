import pandas as pd
import csv
import datetime

header=['日時','名前','時間','出退',]

def write_time(date,name,time,check):
    with open('calculator.csv','a',encoding='UTF-8') as w:
        writer=csv.writer(w)
        writer.writerow(header)
        writer.writerow([date,name,time,check])
