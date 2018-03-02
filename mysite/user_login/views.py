# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Tickets
import django
django.setup()
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    user = authenticate(request, username='bilal', password='test069001')
    if user is not None:
        login(request, user)
        return HttpResponse('login')

    else:
        return HttpResponse('erroe')


