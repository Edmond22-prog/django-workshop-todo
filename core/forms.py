from django import forms


class CreateTaskForm(forms.Form):
    title = forms.CharField(max_length=100)
