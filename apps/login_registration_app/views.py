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


def newBook(request):
	#get authors from DB
	context = {
		'authors': Author.objects.all(),
	}
	#display a form for creating a new book and a review
	return render(request, 'main/new_book.html', context)
	
def indexBook(request):
	duplicate_reviews = Review.objects.order_by('-created_at').all()[3:]
	other_book_reviews = []
	for review in duplicate_reviews:
		if review.book not in other_book_reviews:
			other_book_reviews.append(review.book)

	context = {
		'current_user': current_user(request),
		'recent_book_reviews': Review.objects.order_by('-created_at').all()[:3],
		'other_book_reviews': other_book_reviews,
	}
	return render(request, 'main/books.html', context)
