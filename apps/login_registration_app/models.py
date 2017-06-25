# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt

### Create the models and add additional method to the built in model methods
''' Spelling!!! '''

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	def __str__(self):
		string_output = "first_name: {} last_name: {} email: {} password: {}"

		return string_output.format(
			self.first_name,
			self.last_name,
			self.email,
			self.password,
		)
### one to many relationship: post->user
class Post(models.Model):
	post = models.CharField(max_length=255)
	user = models.ForeignKey(User, related_name="posts")
	likes = models.ManyToManyField(User, related_name="posts_liked")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = PostManager()

class Comment(models.Model):
	comment = models.Textfield()
	post = models.ForeignKey(Post,related_name="comments")
	user = models.ForeignKey(User,related_name="users")
	likes = models.ManyToManyField(User,related_name="comments_liked")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = CommentManager()







