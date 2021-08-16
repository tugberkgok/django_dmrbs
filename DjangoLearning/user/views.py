from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():

        kullaniciadi = form.cleaned_data.get("username")
        sifre = form.cleaned_data.get("password")

        newUser = User(username = kullaniciadi)
        newUser.set_password(sifre)
        newUser.save()
        login(request, newUser)

        return redirect("index")
    context = {"form": form}
    return render(request, "register.html", context)



def loginUser(request):
    form = LoginForm(request.POST or None )
    context = {"form": form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Kullanıcı adı veya sifre hatalı")
            return render(request, "login.html", context)
        login(request, user)
        return redirect("index")

    return render(request, "login.html", context)


def logoutUser(request):

    pass

