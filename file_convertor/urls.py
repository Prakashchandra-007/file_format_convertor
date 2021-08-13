
from django.contrib import admin
from django.urls import path, include
from file_convertor import views
app_name = 'file_convertor'
urlpatterns = [

    path('', views.index, name='index'),
    path('main_page', views.main_page, name='main_page'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name="logout"),
]
