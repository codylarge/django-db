from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), # call the home function in views.py
    path("todos/", views.todos, name="todos")
]