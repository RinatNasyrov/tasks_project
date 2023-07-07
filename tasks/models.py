from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Subsystem(models.Model):
    subsystem_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.subsystem_name}'

class MenuPoint(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT, related_name='child')
    current_subsystem = models.ForeignKey(Subsystem, null=False, blank=False, on_delete=models.PROTECT)

    menu_point_name = models.CharField(max_length=50)
    def get_full_path(self):
        return f'{self.parent.get_full_path()}>{self.menu_point_name}' if self.parent else self.menu_point_name

    def __str__(self):
        return self.get_full_path()

class Task(models.Model):
    class Status(models.TextChoices):
        CREATED = "CR", "В работе"
        REJECTED = "RJ", "Отказано"
        FINISHED = "FN", "Завершено"

    user_to = models.ForeignKey(User, verbose_name='Кому', null=True, blank=True, related_name="actor", on_delete=models.PROTECT, default=None)
    user_from = models.ForeignKey(User, null=True, blank=True, related_name="creator", on_delete=models.PROTECT, default=None)
    menu_point = models.ForeignKey(MenuPoint, null=True, blank=True, on_delete=models.PROTECT, default=None)

    current_status = models.CharField(max_length=2, verbose_name='Статус', choices=Status.choices, default=Status.CREATED)
    description = models.TextField(verbose_name='Описание')
    date_create = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse("cabinet")

    def __str__(self):
        return self.description[:50]



