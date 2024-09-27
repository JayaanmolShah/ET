from django.db import models

# 1) Space Pirate trainer Dx
# 2) Pistol whip 
# 3)Zombieland: Headshot      
#      Fever
# 4)Epic roller coasters 
# 5) Void racer: Extreme 
# 6) Ultimechs


class bgmi_Players(models.Model):
    Rank=models.IntegerField(null=True)
    Team Name = models.CharField(max_length=50,null=True)
    Avatar = models.ImageField(blank=True, null=True)
    KP=models.IntegerField(null=True)
    PP=models.IntegerField(null=True)
    TP=models.IntegerField(null=True)
    game=models.CharField(max_length=50,null=True)
    def __str__(self):
        return f"{self.Name}"
    
class th_Players(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Roll_number=models.CharField(max_length=15,null=True)
    Branch=models.CharField(max_length=20)
    Year=models.CharField(max_length=15)
    Email_id=models.EmailField(null=True)
    Phone=models.IntegerField(null=True)
    DOB=models.DateField(null=True)
    Score=models.IntegerField(null=True)
    Avatar = models.ImageField(upload_to='D:\websocket\ET\ETweb\media\\th', blank=True, null=True)
    Date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    def __str__(self):
        return f"{self.Name}"
    
class vr_Players(models.Model):
    id=models.UUIDField(primary_key=True)
    created_at=models.TimeField(auto_now=True)
    Name = models.CharField(max_length=50,null=True)
    Game = models.CharField(max_length=10)
    Branch=models.CharField(max_length=20)
    Email=models.EmailField(null=True)
    Phone=models.IntegerField(null=True)
    Score=models.IntegerField(default=0)
    play_time = models.DurationField(default=0)
    Avatar = models.CharField( blank=True, null=True)
    Time = models.TimeField(auto_now=True)
    def __str__(self):
        return f"{self.Name}"
