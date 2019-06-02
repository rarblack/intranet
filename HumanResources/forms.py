from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('is_GD',)


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
