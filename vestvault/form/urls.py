from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	url(r'^home$', views.home, name='home'),
]

 #   url(r'^home$', 'home', name='home'),
