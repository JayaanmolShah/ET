from django.db import models

# 1) Space Pirate trainer Dx
# 2) Pistol whip 
# 3)Zombieland: Headshot      
#      Fever
# 4)Epic roller coasters 
# 5) Void racer: Extreme 
# 6) Ultimechs

#1
class vr_pirate_Players(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Roll_number=models.CharField(max_length=15,null=True)
    Branch=models.CharField(max_length=20)
    Year=models.CharField(max_length=15)
    Email_id=models.EmailField(null=True)
    Phone=models.IntegerField(null=True)
    DOB=models.DateField(null=True)
    Score=models.IntegerField(null=True)
    Avatar = models.ImageField(upload_to='D:\websocket\ET\ETweb\media\pirate', blank=True, null=True)
    Date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    def __str__(self):
        return f"{self.Name}"
    
#2    
class vr_pistol_Players(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Roll_number=models.CharField(max_length=15,null=True)
    Branch=models.CharField(max_length=20)
    Year=models.CharField(max_length=15)
    Email_id=models.EmailField(null=True)
    Phone=models.IntegerField(null=True)
    DOB=models.DateField(null=True)
    Score=models.IntegerField(null=True)
    Avatar = models.ImageField(upload_to='D:\websocket\ET\ETweb\media\pistol', blank=True, null=True)
    Date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    def __str__(self):
        return f"{self.Name}"
    
#3    
class vr_zombie_Players(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Roll_number=models.CharField(max_length=15,null=True)
    Branch=models.CharField(max_length=20)
    Year=models.CharField(max_length=15)
    Email_id=models.EmailField(null=True)
    Phone=models.IntegerField(null=True)
    DOB=models.DateField(null=True)
    Score=models.IntegerField(null=True)
    Avatar = models.ImageField(upload_to='D:\websocket\ET\ETweb\media\zombie', blank=True, null=True)
    Date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    def __str__(self):
        return f"{self.Name}"

#4    
class vr_roller_Players(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Roll_number=models.CharField(max_length=15,null=True)
    Branch=models.CharField(max_length=20)
    Year=models.CharField(max_length=15)
    Email_id=models.EmailField(null=True)
    Phone=models.IntegerField(null=True)
    DOB=models.DateField(null=True)
    Score=models.IntegerField(null=True)
    Avatar = models.ImageField(upload_to='D:\websocket\ET\ETweb\media\roller', blank=True, null=True)
    Date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    def __str__(self):
        return f"{self.Name}"

#5
class vr_racer_Players(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Roll_number=models.CharField(max_length=15,null=True)
    Branch=models.CharField(max_length=20)
    Year=models.CharField(max_length=15)
    Email_id=models.EmailField(null=True)
    Phone=models.IntegerField(null=True)
    DOB=models.DateField(null=True)
    Score=models.IntegerField(null=True)
    Avatar = models.ImageField(upload_to='D:\websocket\ET\ETweb\media\racer', blank=True, null=True)
    Date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    def __str__(self):
        return f"{self.Name}"

#6    
class vr_ultimechs_Players(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Roll_number=models.CharField(max_length=15,null=True)
    Branch=models.CharField(max_length=20)
    Year=models.CharField(max_length=15)
    Email_id=models.EmailField(null=True)
    Phone=models.IntegerField(null=True)
    DOB=models.DateField(null=True)
    Score=models.IntegerField(null=True)
    Avatar = models.ImageField(upload_to='D:\websocket\ET\ETweb\media\\ultimechs', blank=True, null=True)
    Date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    def __str__(self):
        return f"{self.Name}"
    
class bgmi_Players(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Rank=models.IntegerField(null=True)
    Avatar = models.ImageField(upload_to='D:\websocket\ET\ETweb\media\\bgmi', blank=True, null=True)
    Date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    FP=models.IntegerField(null=True)
    PP=models.IntegerField(null=True)
    TP=models.IntegerField(null=True)
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