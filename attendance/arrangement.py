import pandas as pd
import csv
import datetime

def write_time(x):
    with open('calculator.csv','a',encoding='UTF-8') as w:
        writer=csv.writer(w)
