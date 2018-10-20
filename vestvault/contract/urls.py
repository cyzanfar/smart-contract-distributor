from django.urls import path
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from contract import views

urlpatterns = [
    path('tokens/', views.TokenList.as_view()),
    path('tokens/<int:pk>/', views.TokenDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
