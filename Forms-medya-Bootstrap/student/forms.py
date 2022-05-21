from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        # fields = {"last_name" : "Surname"}  yapılabilir.   
        # fields = {"first_name","last_name"} bu şekilde istenilen field'larda getirilir.