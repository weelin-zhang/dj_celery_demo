# _*_ coding:utf-8 _*__
from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task

# 模拟一个耗时操作
@shared_task
def longtime_test():
    count = 3
    while count >0:
        print count
        time.sleep(1)
        count-=1
    print 'done'
    return 'done'
