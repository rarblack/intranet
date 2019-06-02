from django import forms


class PasswordChangeForm(forms.Form):
    password1 = forms.CharField()
    password2 = forms.CharField()
