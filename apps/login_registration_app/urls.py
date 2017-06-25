from django.conf.urls import url
from . import views
'''import methods '''

urlpatterns = [
	url(r'^$',views.index)
]