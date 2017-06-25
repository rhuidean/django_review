# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
	print "Inside the index method."
	return render(request,'')
