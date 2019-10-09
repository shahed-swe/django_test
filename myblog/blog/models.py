from django.db import models
import time as t
# Create your models here.
class BlogPost(models.Model):
    slug = models.SlugField(blank=False, unique=True) 
    title = models.CharField(max_length=120)
    content = models.TextField(null = True,blank=True)
    about = models.TextField(null=True)
    time = models.TimeField()
    date = models.DateField()
    select = models.CharField(null = True,max_length=256, choices=[('Model Feed', 'Model Feed'),('News Feed', 'News Feed'),('Other Feed','Other Feed')])