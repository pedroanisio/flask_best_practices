# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 14:42
# @Author  : yangyuexiong
# @Email   : yang6333yyx@126.com
# @File    : interval_test.py
# @Software: PyCharm

import os, sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone='Asia/Shanghai')


# interval: The interval at which the task runs
# (Effective from 2023-1-1 00:00:00 to 2033-1-1 00:00:00, no limit if not set)
# minutes: Minutes
# seconds: Seconds
@sched.scheduled_job('interval', start_date='2023-1-1', end_date='2033-1-1', 
                     seconds=3)
def interval_task():
    print(f'Start execution: {datetime.now()}')
    print('Executing task every 3 seconds...')
    print(f'Execution completed: {datetime.now()}\n')


if __name__ == '__main__':
    print('Testing interval task...')
    print(datetime.now())
    sched.start()
