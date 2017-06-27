# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
### one-time flash messages
from django.contrib import messages
from django.db.models import Count
from .models import *

def index(request):
	return render(request,'login_registration_app/index.html')
