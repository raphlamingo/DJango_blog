from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create'),
    path('update_form/<str:pk>',views.update, name='update'),
    path('post/<str:pk>', views.read, name='read'),
    path('register/', views.create_user, name='register'),
    path('about/<str:pk>', views.about, name= 'about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout_user'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('about_user/', views.about_user, name='userinfo'),
    path('update_user/', views.update_user, name='update_user'),
    path('profile/', views.profile, name='profile'),
    path('search/',views.find, name='search'),
    path('result/<str:pk>', views.result, name='result')
]
