from django.forms import ModelForm, ModelChoiceField

from tasks.models import Task, MenuPoint

#Формы можно использовать для корректииирования вывода даннных из модели
class TaskCreateModelForm(ModelForm):

    menu_point = ModelChoiceField(queryset=MenuPoint.objects.filter(child__isnull=True), label='Пункт меню')

    class Meta:
        model = Task
        exclude = ['user_from', 'date_create']
