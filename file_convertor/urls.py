
from django.contrib import admin
from django.urls import path, include
from file_convertor import views

app_name = 'file_convertor'
urlpatterns = [
    path('', views.main_page),
    path('landing', views.main_page, name='index'),
    path('main_page', views.upload_file, name='main_page'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name="logout"),
    path('conver', views.conver, name='conver'),
    path('download_page', views.download_page, name="download_page"),
    path('download/', views.download_file, name="download"),
]
