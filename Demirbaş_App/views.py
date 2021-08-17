from django.shortcuts import render, HttpResponse

# Create your views here.
def Main(request):
    return render(request, "Main.html")
