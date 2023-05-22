from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Rabs
from .models import Rabs2
from .models import Img
from .models import Zap1
from .models import Zap2
from .models import Zap3

def kazan_home(request):
    rabs = Img.objects.all()
    return render(request, 'main/kazan.html', {'rabs': rabs})

def moscow_home(request):
    rabs = Img.objects.all()
    return render(request, 'main/msc.html', {'rabs': rabs})

def kazan_appointment(request):
    rabs = Rabs.objects.all()
    return render(request, 'main/zapiskaz.html', {'rabs': rabs})

def appointmentMOSCOW(request):
    rabs = Rabs2.objects.all()
    return render(request, 'main/zapismsc.html', {'rabs': rabs})

def create1(request):

    if request.method == "POST":
        zap = Zap1()
        zap.name = request.POST.get("name")
        zap.phone = request.POST.get("phone")
        #zap.doctor = request.POST.get("doctor")
        zap.save()
    return HttpResponseRedirect("/")

def rrr(request):

    if request.method == "POST":
        zap = Zap2()
        zap.name = request.POST.get("name")
        zap.phone = request.POST.get("phone")
        #zap.doctor = request.POST.get("doctor")
        zap.save()
    return HttpResponseRedirect("/")

def create3(request):

    if request.method == "POST":
        zap = Zap3()
        zap.name = request.POST.get("name")
        zap.phone = request.POST.get("phone")
        #zap.doctor = request.POST.get("doctor")
        zap.save()
    return HttpResponseRedirect("/")