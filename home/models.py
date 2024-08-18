from django.db import models

# Create your models here.
class Players(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Roll_number=models.CharField(max_length=15,null=True)
    Branch=models.CharField(max_length=20)
    Year=models.CharField(max_length=15)
    Email_id=models.EmailField(null=True)
    Phone=models.IntegerField(null=True)
    DOB=models.DateField(null=True)
    Score=models.IntegerField(null=True)
    Avatar = models.ImageField(upload_to='D:\websocket\ET\ETweb\media', blank=True, null=True)
    Date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    def __str__(self):
        return f"{self.Name}"