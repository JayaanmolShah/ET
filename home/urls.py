from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("vr_home",views.vr_home,name='vr_home'),
    path("bgmi_home",views.bgmi_home,name='bgmi_home'),
    path("th_home",views.th_home,name='th_home'),
    path("scoreboard",views.scoreboard,name='scoreboard'),
    path("vr_game1",views.vr_game1,name='vr_game1'),
    path("vr_game2",views.vr_game2,name='vr_game2'),
    path("vr_game3",views.vr_game3,name='vr_game3'),
    path("bgmi_reg",views.bgmi_reg,name='bgmi_reg'),

]
