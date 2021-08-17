from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Worker
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.
def Main(request):
    data = Worker.objects.all()
    return render(request, "Main.html", {"veri" : data})

def delete(request, person):
    worker = get_object_or_404(Worker, person = person)
    worker.delete()
    return redirect("main")


def loginUser(request):
    form = LoginForm(request.POST or None )
    context = {"form": form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, "login.html", context)
        login(request, user)
        return redirect("main")

    return render(request, "login.html", context)


def logoutUser(request):

    pass
