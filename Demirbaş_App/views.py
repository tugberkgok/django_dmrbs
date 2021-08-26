import os
import sqlite3
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from xlsxwriter.workbook import Workbook

from .models import Worker, Device
from .forms import RegisterForm, LoginForm, DataForm, WorkerName
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

@login_required(login_url = 'login')
def Main(request):
    data = Worker.objects.all()
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

        return redirect("main")

    if keyword:
        data = Worker.objects.filter(person__contains=keyword)
        return render(request, "Main.html", {"veri": data})

    return render(request, "Main.html", {"veri": data})

@login_required(login_url='login')
def update(request, id):
    datas = Device.objects.filter(person_id=id)
    person = Worker.objects.filter(id=id)
    superuser = Worker.objects.filter(superuser=True)
    devices = Device.objects.all()
    workers = Worker.objects.all()
    super = 1
    if person[0] in superuser:
        return render(request, "update.html", {"datas": devices, "name": person[0], "workers": workers, "super": super})
    else:
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
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            fail = 1
            return render(request, "login.html", {"form": form, "fail": fail})
        login(request, user)
        return redirect("main")
    return render(request, "login.html", {"form": form})


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

def excel(request, id):
    person = Worker.objects.filter(id=id)
    conn = sqlite3.connect('db.sqlite3')
    query1 = "SELECT id FROM Demirbaş_App_worker WHERE person = '{}'".format(person[0])
    result1 = conn.cursor()
    result1.execute(query1)
    pid = result1.fetchone()
    query2 = "SELECT stok, device, number, brand, model, serial, status, exp FROM Demirbaş_App_device WHERE person_id_id = '{}'".format(pid[0])
    result2 = conn.cursor()
    result2.execute(query2)
    data = result2.fetchall()
    workbook = Workbook(os.path.join(os.path.join(os.environ['USERPROFILE'])) + "\\Desktop\\{}.xlsx".format(person[0]))
    worksheet = workbook.add_worksheet()
    worksheet.set_column(
        "C:C", 5

    )
    worksheet.set_column(
        "F:F",
        30
    )
    cell_format1 = workbook.add_format({'bold': True, 'italic': False})

    worksheet.write('A1', 'DEMİRBAŞ ENVANTER LİSTESİ', cell_format1)
    worksheet.write('A3', 'STOK', cell_format1)
    worksheet.write('B3', 'CİHAZ', cell_format1)
    worksheet.write('C3', 'SAYI', cell_format1)
    worksheet.write('D3', 'MARKA', cell_format1)
    worksheet.write('E3', 'MODEL', cell_format1)
    worksheet.write('F3', 'SERİ NO', cell_format1)
    worksheet.write('G3', 'DURUMU', cell_format1)
    worksheet.write('H3', 'AÇIKLAMA', cell_format1)
    row = 0
    cell = 0
    for row, veri in enumerate(data):
        for cell, value in enumerate(veri):
            print(value)
            if str(value) == "None":
                worksheet.write(row + 3, cell -1, value)
            else:
                worksheet.write(row + 3, cell, value)
    cell = 0
    row = row + 5
    worksheet.write(row, cell, "Yukarıda listelenen .......... malzemeyi sağlam olarak teslim aldım", cell_format1)
    worksheet.write(row + 1, cell, "Tesliim Alan: ", cell_format1)
    worksheet.write(row + 1, cell + 4, "Tesliim Eden: ", cell_format1)
    worksheet.write(row + 2, cell, "İmzası: ", cell_format1)
    worksheet.write(row + 2, cell + 4, "İmzası: ", cell_format1)
    workbook.close()
    conn.close()
    return redirect("/update/{}".format(pid[0]))

def dropdown(request, id, pid):
    person = Worker.objects.filter(id=pid)

    conn = sqlite3.connect('db.sqlite3')
    query1 = "SELECT id FROM Demirbaş_App_worker WHERE person = '{}'".format(person[0])
    result1 = conn.cursor()
    result1.execute(query1)
    data = result1.fetchone()
    cursor = conn.cursor()
    query2 = "UPDATE Demirbaş_App_device SET person_id_id = '{}' WHERE id = {}".format(data[0], id)
    cursor.execute(query2)
    conn.commit()
    conn.close()

    return redirect("/update/30")

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        key = form.cleaned_data.get("special_key")

        

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()

        return redirect("login")

    context = {"form": form}    
    return render(request, "register.html", context)


def superregister(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        key = form.cleaned_data.get("special_key")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        
        return redirect("login")

    context = {"form": form}
    return render(request, "superregister.html", context)