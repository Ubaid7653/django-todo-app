from django.contrib import admin
from django.urls import path
from ToDo_App import views

urlpatterns = [
    path('todo_app', views.todo_app, name='todo_app'),
    path('about', views.about, name='about'),
]