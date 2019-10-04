from django.db import models
import time as t
# Create your models here.
class BlogPost(models.Model):
    slug = models.SlugField(blank=False, unique=True) 
    title = models.TextField()
    content = models.TextField(null = True,blank=True)
    about = models.TextField(null=True)
    time = models.TimeField()
    date = models.DateField()