from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Status(models.Model):
    staus_name = models.CharField(max_length=15)

class MenuPoint(models.Model):
    menu_point_name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child', on_delete=models.PROTECT())

    def get_full_path(self):
        return self.parent.get_full_path() + [self.menu_point_name] if self.parent else [self.menu_point_name]

class Task(models.Model):
    user_to = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT())
    current_status =models.ForeignKey(Status, null=False, blank=False, on_delete=models.PROTECT())

    menu_point = models.ForeignKey(MenuPoint, null=False, blank=False, on_delete=models.PROTECT())
    description= models.TextField()
    date_create = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse("cabinet")

class Subsystem(models.Model):
    subsystem_name = models.CharField(max_length=30)

