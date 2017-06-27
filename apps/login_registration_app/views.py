# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
### one-time flash messages
from django.contrib import messages
from django.db.models import Count
from .models import *

def index(request):
	return render(request,'login_registration_app/index.html')

def showBook(request, id):
	book = Book.objects.filter(id=id).first()
	context = {
		'book': book,
		'reviews': book.reviews.select_related('user').all(),
		'current_user': current_user(request),
	}
	return render(request, 'main/show_book.html', context)