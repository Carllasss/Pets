from django import forms


class TaskForm(forms.Form):
    title = forms.CharField()
    pet = forms.CharField()
    age = forms.IntegerField()
    type = forms.CharField()


class PhotoForm(forms.Form):
    url = forms.CharField()
