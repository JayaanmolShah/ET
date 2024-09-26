from django.shortcuts import render,HttpResponse
from django.core.files.base import ContentFile
from home.models import vr_Players,bgmi_Players,th_Players
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

def scoreboard(request,game):
    if game=='vr':
        players = vr_Players.objects.all().order_by('-Score')
    elif game=='pirate':
        players = vr_Players.objects.filter(Game='Pirate').order_by('-Score')
        # players = th_Players.objects.all().order_by('-Score')
    elif game=='roller':
        players = vr_Players.objects.filter(Game='Roller').order_by('-Score')
        # players = th_Players.objects.all().order_by('-Score')
    elif game=='th':
        players = th_Players.objects.all().order_by('-Score')
    
    return render(request,'scoreboard.html',{'players': players})

def scoreboard2(request):
    players = bgmi_Players.objects.all().order_by('Rank')
    return render(request,'scoreboard2.html',{'players': players})