import pandas as pd
import csv,os
import datetime
import json

def write_time(date,name,time,check):
    with open('calculator.csv','a',encoding='UTF-8') as w:
        writer=csv.writer(w)
        writer.writerow([date,name,time,check])





    

