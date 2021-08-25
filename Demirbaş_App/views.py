import sqlite3
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Worker, Device
from .forms import RegisterForm, LoginForm, DataForm, WorkerName
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json

# Create your views here.

@login_required(login_url = 'login')
def Main(request):

    keyword = request.GET.get("keyword")
    key = request.GET.get("key")
    if key:
        stok = Device.objects.filter(stok__contains=key)
        device = Device.objects.filter(device__contains=key)
        brand = Device.objects.filter(brand__contains=key)
        model = Device.objects.filter(model__contains=key)
        serial = Device.objects.filter(serial__contains=key)
        status = Device.objects.filter(status__contains=key)
        exp = Device.objects.filter(exp__contains=key)
        liste = []
        if stok:
            for idx in stok:
                datas = Worker.objects.filter(person=idx)
                liste.append(datas[0])
            return render(request, "Main.html", {"veri": liste})
        elif device:
            for idx in device:
                datas = Worker.objects.filter(person=idx)
                liste.append(datas[0])
            return render(request, "Main.html", {"veri": liste})
        elif brand:
            for idx in brand:
                datas = Worker.objects.filter(person=idx)
                liste.append(datas[0])
            return render(request, "Main.html", {"veri": liste})
        elif model:
            for idx in model:
                datas = Worker.objects.filter(person=idx)
                liste.append(datas[0])
            return render(request, "Main.html", {"veri": liste})
        elif serial:
            for idx in serial:
                datas = Worker.objects.filter(person=idx)
                liste.append(datas[0])
            return render(request, "Main.html", {"veri": liste})
        elif status:
            for idx in status:
                datas = Worker.objects.filter(person=idx)
                liste.append(datas[0])
            return render(request, "Main.html", {"veri": liste})
        elif exp:
            for idx in exp:
                datas = Worker.objects.filter(person=idx)
                liste.append(datas[0])
            return render(request, "Main.html", {"veri": liste})
        #datas = Worker.objects.filter(person=data[0])

        #return render(request, "Main.html", {"veri": datas})
        return redirect("main")

    if keyword:
        data = Worker.objects.filter(person__contains=keyword)
        return render(request, "Main.html", {"veri": data})
    data = Worker.objects.all()
    return render(request, "Main.html", {"veri": data})
def search(request):
    pass


@login_required(login_url='login')
def update(request, id):
    datas = Device.objects.filter(person_id=id)
    person = Worker.objects.filter(id=id)
    try:
        if datas[0] != " ":
            return render(request, "update.html", {"datas": datas, "name": person[0]})
    except:
        return render(request, "update.html", {"name": person[0]})

@login_required(login_url = 'login')
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

@login_required(login_url = 'login')
def addPerson(request):
    form = WorkerName(request.POST or None)
    if form.is_valid():
        conn = sqlite3.connect('db.sqlite3')
        query = "SELECT person FROM Demirbaş_App_worker WHERE person = '{}'".format(str(form["person"].value()))
        result = conn.cursor()
        result.execute(query)
        name = result.fetchone()
        conn.close()
        try:
            if str(form["person"].value()) != str(name[0]):
                form.save()
                messages.success(request, "Kişi Kaydedildi")
                return redirect("main")
            else:
                return render(request, "addPerson.html", {"form": form, "name": name})
        except:
            form.save()
            messages.success(request, "Kişi Kaydedildi")
            return redirect("main")
    else:
        return render(request, "addPerson.html", {"form": form})


@login_required(login_url = 'login')
def addData(request, id):
    person = Worker.objects.filter(id=id)
    form = DataForm(request.POST or None)
    if form.is_valid():
        conn = sqlite3.connect('db.sqlite3')
        query1 = "SELECT id FROM Demirbaş_App_worker WHERE person = '{}'".format(person[0])
        result = conn.cursor()
        result.execute(query1)
        pid = result.fetchone()
        query2 = "INSERT INTO Demirbaş_App_device (stok, device, number, brand, model, serial, status, exp, person_id_id) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"\
                .format(str(form["stok"].value()), str(form["device"].value()), str(form["number"].value()), str(form["brand"].value()), str(form["model"].value()),
                        str(form["serial"].value()), str(form["status"].value()), str(form["exp"].value()), pid[0])
        c = conn.cursor()
        c.execute(query2)
        conn.commit()
        conn.close()
        return redirect("/update/{}".format(pid[0]))

    return render(request, "addData.html", {"form": form})


@login_required(login_url = 'login')
def objectEdit(request, id):
    datas = Device.objects.filter(id=id)
    conn = sqlite3.connect('db.sqlite3')
    query = "SELECT id FROM Demirbaş_App_worker WHERE person = '{}'".format(datas[0])
    result = conn.cursor()
    result.execute(query)
    pid = result.fetchone()
    conn.close()
    form = DataForm(request.POST or None, request.FILES or None, instance=get_object_or_404(Device, id=id))
    if form.is_valid():
        form.save()
        return redirect("/update/{}".format(pid[0]))

    return render(request, "objectEdit.html", {"form": form})

@login_required(login_url = 'login')
def objectDelete(request, id):
    object = Device.objects.filter(id=id)
    conn = sqlite3.connect('db.sqlite3')
    query = "SELECT id FROM Demirbaş_App_worker WHERE person = '{}'".format(object[0])
    result = conn.cursor()
    result.execute(query)
    pid = result.fetchone()
    conn.close()
    object.delete()
    return redirect("/update/{}".format(pid[0]))
