from . models import Todo
from django import forms
class Todoform(forms.ModelForm):
    class Meta:
        model= Todo
        fields = ['task', 'priority', 'time']