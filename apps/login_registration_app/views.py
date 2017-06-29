# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
### one-time flash messages
from django.contrib import messages
from django.db.models import Count
from .models import *

def index(request):
	return render(request,'login_registration_app/index.html')

def createUser(request):
	if request.method != 'POST':
		return redirect('/')
	attempt = User.objects.validateUser(request.POST)
	if attempt['status'] == True:
		user = User.objects.createUser(request.POST)
		request.session['user_id'] = user.id
		return redirect('/books')
	else:
		for error in attempt['errors']:
			messages.add_message(request, messages.ERROR, error, extra_tags="registration")
			return redirect('/')

def loginUser(request):
	if request.method != 'POST':
		return redirect('/')
	attempt = User.objects.validateUser(request.POST)
	if attempt['status']== True:
		request.session['user_id']=attempt['user'].id
		return redirect('/')
	else:
		messages.add_message(request,messages.ERROR,)
		return redirect('/')

def showBook(request, id):
	book = Book.objects.filter(id=id).first()
	context = {
		'book': book,
		'reviews': book.reviews.select_related('user').all(),
		'current_user': current_user(request),
	}
	return render(request, 'main/show_book.html', context)