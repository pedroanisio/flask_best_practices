# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 14:42
# @Author  : yangyuexiong
# @Email   : yang6333yyx@126.com
# @File    : cron_test.py
# @Software: PyCharm

import os, sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))

from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone='Asia/Shanghai')


# cron periodic task execution (runs within a specific time range)
# Runs every Monday to Friday from 2023-1-1 to 2023-12-31
# at 6:01:01 AM
@sched.scheduled_job('cron', start_date='2023-1-1', end_date='2023-12-31',
                      day_of_week='mon-fri', hour=6, minute=1, second=1)
def cron_task():
    print(f'Start execution: {datetime.now()}')
    print('Executing task...')
    print(f'Execution complete: {datetime.now()}\n')


if __name__ == '__main__':
    print('Testing cron ...')
    print(datetime.now())
    sched.start()
