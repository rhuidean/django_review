# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect

def index(request):
	print "Inside the index method."
	return render(request,'django_review_app/index.html')
