from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="zkt/home/static/images")