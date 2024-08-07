from django.db import models
from django.utils import timezone
from Movies.models import Genere
from customers.models import Customer 

    

class Series(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    priority=models.IntegerField(default=0)
    name=models.CharField(max_length=30,null=False)
    description=models.TextField()
    rating=models.FloatField(null=False)
    genere=models.ManyToManyField(Genere,related_name='accociated_genere')
    censor_info=models.CharField(max_length=30,null=False)
    no_of_seasons=models.CharField(max_length=30,null=False)
    quality=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    running_time=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
    poster=models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.name
    
    
class Trailer(models.Model):
    owner=models.ForeignKey(Series,related_name='series_name',on_delete=models.SET_NULL,null=True)
    season=models.IntegerField(null=False)
    link=models.TextField()
    
    
class SeriesComments(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    owner=models.ForeignKey(Series,related_name='series_name1',on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(Customer,related_name='person',on_delete=models.CASCADE)
    comment=models.CharField(null=False,max_length=250)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment
    
    
    
class SeriesReview(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    owner=models.ForeignKey(Series,related_name='series_name2',on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(Customer,related_name='asscociated_person',on_delete=models.CASCADE)
    review=models.TextField(null=False)
    title=models.CharField(max_length=100,null=True)
    rating=models.FloatField(null=False)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return self.review
    

class Season(models.Model):
    owner=models.ForeignKey(Series,on_delete=models.CASCADE,related_name='season_of')
    start=models.DateField()
    end=models.DateField()
    no_of_episodes=models.CharField(max_length=10)
    season_no=models.CharField(max_length=10)
    
    def __str__(self):
        return self.season_no
    