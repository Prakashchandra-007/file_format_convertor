
from django.contrib import admin
from django.urls import path, include
from file_convertor import views

app_name = 'file_convertor'
urlpatterns = [

    path('', views.user_login, name='index'),
    path('main_page', views.upload_file, name='main_page'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name="logout"),
    path('conver', views.conver, name='conver')
]
