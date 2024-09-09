from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("vr_home",views.vr_home,name='vr_home'),
    path("bgmi_home",views.bgmi_home,name='bgmi_home'),
    path("th_home",views.th_home,name='th_home'),
    path("scoreboard/<str:game>/",views.scoreboard,name='scoreboard'),
]
