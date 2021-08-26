"""Demirbaş_Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Demirbaş_App import views


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.loginUser, name="login"),
    path('main', views.Main, name="main"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('logout/', views.logoutUser, name="lagout"),
    path('update/<str:id>', views.update, name="update"),
    path('addData/<int:id>', views.addData, name="addData"),
    path('addPerson', views.addPerson, name="addPerson"),
    path('object/edit/<int:id>', views.objectEdit, name="objectEdit"),
    path('object/delete/<int:id>', views.objectDelete, name="objectEdit"),
    path('person/excel/<int:id>', views.excel, name="excel"),
    path('dropdown/<int:id>-<int:pid>', views.dropdown, name="dropdown"),
    #path('adminpassword', views.adminpassword, name="adminpassword"),
    path('register', views.register, name="register"),

]
