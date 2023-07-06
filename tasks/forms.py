from django.forms import ModelForm, ModelChoiceField

from tasks.models import Task, MenuPoint


class TaskCreateModelForm(ModelForm):

    menu_point = ModelChoiceField(queryset=MenuPoint.objects.filter(child__isnull=True))

    class Meta:
        model = Task
        exclude = ['user_from', 'date_create']
