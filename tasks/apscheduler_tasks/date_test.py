# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 14:50
# @Author  : yangyuexiong
# @Email   : yang6333yyx@126.com
# @File    : date_test.py
# @Software: PyCharm

import os, sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone='Asia/Shanghai')


# Date-based scheduled task for a specific execution date
# Executes on September 5, 2023
# @sched.scheduled_job('date', run_date=date(2023, 9, 5), args=['text'])
@sched.scheduled_job('date', run_date=datetime(2023, 9, 5, 10, 31, 5), args=['text'])  # Executes on Sep 5, 2023, 10:31:05
def date_and_datetime_task(text):
    print('Date/Datetime Scheduled Task', 'Parameter: {}'.format(text))


if __name__ == '__main__':
    print('Testing date scheduling...')
    print(datetime.now())
    sched.start()
