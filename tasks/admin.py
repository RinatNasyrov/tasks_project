from django.contrib import admin
from .models import Subsystem, MenuPoint, Task
# Register your models here.
admin.site.register(Subsystem)
admin.site.register(MenuPoint)
admin.site.register(Task)
