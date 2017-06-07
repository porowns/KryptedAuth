from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from core.models import Profile, Notification, Game

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32)

    def clean(self):
        input = self.cleaned_data

        if authenticate(username=input.get('username'),
         password=input.get('password')) is not None:
            pass
        else:
            self.add_error('username', 'Invalid credentials.')

        return input

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=32)
    email = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32)
    vpassword = forms.CharField(max_length=32)

    def clean(self):
        input = self.cleaned_data
        password = input.get('password')

        if User.objects.filter(username=input.get('username')).exists():
            self.add_error('username', "Username is taken.")
        if password:
            if input.get('password') != input.get('vpassword'):
                self.add_error('password', 'Passwords do not match.')
            if len(password) < 8:
                self.add_error('password', 'Password must be 8 characters or more.')

        return input

class ProfileForm(forms.Form):
    games = forms.ModelChoiceField(queryset=Game.objects.all(), empty_label="None")

class NotificationForm(forms.Form):
    title = forms.CharField(max_length=24)
    text = forms.CharField(max_length=500)
    game = forms.ModelChoiceField(queryset=Game.objects.all(), empty_label="None")

class GameForm(forms.Form):
    title = forms.CharField(max_length=24)
