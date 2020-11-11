from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"  # include all fields
        # fields = ('title', 'completed')

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter task description...",
            }
        ),
    )

    completed = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxInput(
            attrs={
                "class": "form-check-input",
            }
        ),
    )

# For more about Django Forms, see:
# https://www.webforefront.com/django/formfieldtypesandvalidation.html