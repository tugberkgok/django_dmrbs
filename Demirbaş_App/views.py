from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Worker
# Create your views here.
def Main(request):
    data = Worker.objects.all()
    return render(request, "Main.html", {"veri" : data})

def delete(request, person):
    worker = get_object_or_404(Worker, person = person)
    worker.delete()
    return redirect("main")
