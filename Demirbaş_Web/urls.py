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
    path('delete/confirm/<int:id>', views.personConfirm, name="workerConfirm"),
    path('deleteUser/confirm/<int:id>', views.userConfirm, name="userConfirm"),
    path('deleteUser/<int:id>', views.userDelete, name="userDelete"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('logout/', views.logoutUser, name="lagout"),
    path('update/logout', views.logoutUser, name="lagout"),
    path('addData/logout', views.logoutUser, name="lagout"),
    path('allData', views.allData, name="allData"),
    path('update/<int:id>', views.update, name="update"),
    path('addData/<int:id>', views.addData, name="addData"),
    path('addPerson', views.addPerson, name="addPerson"),
    path('object/edit/<int:id>', views.objectEdit, name="objectEdit"),
    path('object/confirm/<int:id>', views.objectConfirm, name="objectConfirm"),
    path('object/delete/<int:id>', views.objectDelete, name="objectDelete"),
    path('person/excelwrite/<int:id>', views.excelwrite, name="excelwrite"),
    # path('person/excelread/<int:id>', views.excelread, name="excelread"),
    path('dropdown/<int:id>-<int:pid>', views.dropdown, name="dropdown"),
    path('dropdownAll/<int:id>-<int:pid>', views.dropdownAll, name="dropdown"),
    path('confirm/<int:id>-<int:pid>', views.dropConfirm, name="dropConfirm"),
    path('confirmAll/<int:id>-<int:pid>', views.dropConfirmAll, name="dropConfirm"),
    path('superregister', views.superregister, name="superregister"),
    path('register', views.register, name="register"),
    path('users', views.users, name="users"),
    path('update/upload/<int:id>', views.excelread, name="upload"),
    path('allExcelwrite', views.allExcelwrite, name="allExcelwrite"),
    path('about', views.about, name="about"),
    path('history', views.history, name="history")
]
