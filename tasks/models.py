from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description= models.TextField()
    date_create = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse("cabinet")