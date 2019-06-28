from .models import Project
from django import forms
from django.forms import ModelForm, Textarea, IntegerField

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']