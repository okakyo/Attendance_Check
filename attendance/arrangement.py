import pandas as pd
import csv,os
import datetime
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def spread_sheet(date,name,time,check):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project -09445820316a.json', scope)

    gc = gspread.authorize(credentials)

    SPREADSHEET_KEY = '1lqF7o26iuWTvOvOM-v3x5zpa7P3bJrsH2wZIC-fBN9A'

    wks = gc.open_by_key(SPREADSHEET_KEY).sheet1

    wks.append_row([date,name,time,check])

def write_time(date,name,time,check):
    with open('calculator.csv','a',encoding='UTF-8') as w:
        writer=csv.writer(w)
        writer.writerow([date,name,time,check])