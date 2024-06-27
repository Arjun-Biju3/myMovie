from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    name=models.CharField(max_length=100,null=False)
    email=models.EmailField(null=False)
    password=models.TextField(max_length=15)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    
