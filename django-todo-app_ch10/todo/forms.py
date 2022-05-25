
from django import forms
from .models import Todo
from django.db.models import fields

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields = "__all__"