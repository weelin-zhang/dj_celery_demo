# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .tasks import longtime_test
from proj.celery import debug_task
# Create your views here.


def test_view(request):
    r = longtime_test.delay()
    print dir(r)
    print r.state
    print r.id
    return HttpResponse('ok')

def test_debug(request):
    r = debug_task.delay()
    print dir(r)
    print r.state
    print r.id
    return HttpResponse('ok')
