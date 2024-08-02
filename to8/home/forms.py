from django import forms
from .models import Todo


class CreatedataForm(forms.Form):
    title = forms.CharField(required=False, max_length=200)
    body = forms.CharField()
    date_created = forms.DateTimeField()


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'body', 'date_created']

