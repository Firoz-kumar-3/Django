from django import forms
from .models import Student

class UserForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ("name","email","password")
