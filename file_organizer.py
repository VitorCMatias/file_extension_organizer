#!/usr/bin/env python3
import os
import shutil
import time
from datetime import date
import datetime


def calculate_time_interval(month: int) -> datetime.timedelta:
    time_interval = datetime.timedelta(days=30 * month)
    return time_interval


def get_file_creation_date(file: str) -> datetime.date:
    creation_date_epoch = os.path.getctime(file)
    creation_date = datetime.datetime.strptime(time.ctime(creation_date_epoch), "%a %b %d %H:%M:%S %Y")
    return creation_date.date()


if not os.path.isdir('./PDFs'):
    os.mkdir('PDFs')

for filename in os.listdir("./"):
    if filename.endswith('.pdf'):
        today = date.today()
        file_creation_date = get_file_creation_date(filename)

        if today > (file_creation_date + calculate_time_interval(6)):
            shutil.move('./'+filename, './PDFs/'+filename)
