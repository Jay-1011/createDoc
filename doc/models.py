from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

class MyModel(models.Model):
    email= models.EmailField(max_length=50,blank=True)
    date= models.DateTimeField(default=timezone.now)
    number= models.BigIntegerField(blank=True,null=True)
    title = models.CharField(max_length=200, blank=True)
    description=models.TextField(blank=True)
    centertxt = models.CharField(max_length=200,blank=True)
    signature = models.CharField(max_length=200,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self):
        return self.title


class Document(models.Model):
    email = models.EmailField(max_length=50, blank=True)
    date = models.DateTimeField(default=timezone.now)
    number = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    centertxt = models.CharField(max_length=200, blank=True)
    signature = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.title