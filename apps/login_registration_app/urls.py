from django.conf.urls import url
from . import views
'''import methods '''


### Similar to node express server routes
urlpatterns = [
	url(r'^$',views.index),
	url(r'^$users$',views.createUser),
]