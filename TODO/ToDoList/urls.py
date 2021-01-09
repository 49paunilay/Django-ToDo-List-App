from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.todo ,name='todo'),
    path('update/<str:primary_key>/',views.updateTask,name="update"),
    path('delete/<str:primary_key>/',views.deleteTask,name="delete")
]
