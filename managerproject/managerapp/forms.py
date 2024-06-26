from django import forms
from django.contrib.auth.models  import User

from .models import Task


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    username=forms.CharField(error_messages='',max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=('username','email')
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    

class CreateTaskForm(forms.ModelForm):

    class Meta:

        model = Task
        fields = ['name', 'description',]
        exclude = ['assigned_person',]