from django.db import models
from django.utils import timezone
from customers.models import Customer

class Genere(models.Model):
    title=models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
    

class Movies(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    priority=models.IntegerField(default=0)
    name=models.CharField(max_length=30,null=False)
    description=models.TextField()
    rating=models.FloatField(null=False)
    genere=models.ManyToManyField(Genere,related_name='genere_name')
    censor_info=models.CharField(max_length=30,null=False)
    quality=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    running_time=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
    poster=models.ImageField(upload_to='media/')
    trailer=models.TextField()
    
    def __str__(self):
        return self.name
    
    
class MovieComments(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    owner=models.ForeignKey(Movies,related_name='movie_name',on_delete=models.CASCADE)
    user=models.ForeignKey(Customer,related_name='associated_user',on_delete=models.CASCADE)
    comment=models.TextField(null=False)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(timezone.now)
    
    def __str__(self):
        return self.comment
    
    
class MovieReview(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    owner=models.ForeignKey(Movies,related_name='movie_name1',on_delete=models.CASCADE)
    user=models.ForeignKey(Customer,related_name='person1',on_delete=models.CASCADE)
    review=models.CharField(max_length=30,null=False)
    description=models.TextField()
    rating=models.FloatField()
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(timezone.now)    
    
    def __str__(self):
        return self.review
    
    
    
    
    
    
    
    
