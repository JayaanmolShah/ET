from django.shortcuts import render,HttpResponse
from django.core.files.base import ContentFile
from home.models import Players
import datetime


# Create your views here.
def index(request):
    return render(request,'index.html')

def vr_home(request):
    return render(request,'vr_home.html')

def bgmi_home(request):
    return render(request,'bgmi_home.html')

def th_home(request):
    return render(request,'th_home.html')

def vr_game1(request):
    return render(request,'vr_game1.html')

def vr_game2(request):
    return render(request,'vr_game2.html')

def vr_game3(request):
    return render(request,'vr_game3.html')

def bgmi_reg(request):
    return render(request,'bgmi_reg.html')

def scoreboard(request):
    players = Players.objects.all().order_by('-Score')
    return render(request,'scoreboard.html',{'players': players})

