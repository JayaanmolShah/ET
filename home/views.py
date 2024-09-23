from django.shortcuts import render,HttpResponse
from django.core.files.base import ContentFile
from home.models import vr_pirate_Players,vr_pistol_Players,vr_racer_Players,vr_roller_Players,vr_ultimechs_Players,vr_zombie_Players,bgmi_Players,th_Players
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
    if game=='pirate':
        players = vr_pirate_Players.objects.all().order_by('-Score')
    elif game=='zombie':
        players = vr_zombie_Players.objects.all().order_by('-Score')
    elif game=='pistol':
        players = vr_pistol_Players.objects.all().order_by('-Score')
    elif game=='racer':
        players = vr_racer_Players.objects.all().order_by('-Score')
    elif game=='roller':
        players = vr_roller_Players.objects.all().order_by('-Score')
    elif game=='ultimechs':
        players = vr_ultimechs_Players.objects.all().order_by('-Score')
    elif game=='bgmi':
        players = bgmi_Players.objects.all().order_by('-Score')
    elif game=='th':
        players = th_Players.objects.all().order_by('-Score')
    
    return render(request,'scoreboard.html',{'players': players})

def scoreboard2(request):
    players = bgmi_Players.objects.all().order_by('Rank')
    return render(request,'scoreboard2.html',{'players': players})