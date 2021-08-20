from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Worker, Device
from .forms import RegisterForm, LoginForm, DataForm, WorkerName
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def Main(request):
    data = Worker.objects.all()
    return render(request, "Main.html", {"veri" : data})

def update(request, id):
    datas = Device.objects.filter(person_id=id)
    person = Worker.objects.filter(id=id)
    try:
        if datas[0] != " ":
            return render(request, "update.html", {"datas": datas, "name" :person[0]})
    except:
        return render(request, "update.html", {"name": person[0]})

def delete(request, id):
    worker = get_object_or_404(Worker, id=id)
    worker.delete()
    return redirect("main")

def loginUser(request):
    form = LoginForm(request.POST or None)
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
    logout(request)
    return redirect("/")

def dashboard(request):
    pass

def addPerson(request):
    form = WorkerName(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Kişi Kaydedildi")
        return redirect("main")
    return render(request, "addPerson.html", {"form": form})

def addData(request):
    form = DataForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Veri Kaydedildi", )
        return redirect("dashboard")

    return render(request, "addData.html", {"form": form})