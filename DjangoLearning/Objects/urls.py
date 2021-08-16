from django.contrib import admin
from django.urls import path
from . import views

app_name = "object"


urlpatterns = [

    path('update/', views.index, name="index"),
    path('search/', views.index, name="index"),


]
