from django.shortcuts import render

# Create your views here.

def intranet(request):
    return render(request, "intranet.html")

def aplicativos(request):
    return render(request, "aplicativos.html")