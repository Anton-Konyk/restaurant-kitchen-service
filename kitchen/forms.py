
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, PasswordResetForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from kitchen.models import Cook


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "Username"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg", "placeholder": "Password"}),
    )


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Email'
    }))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label=_("Password Confirmation"),
        widget=forms.PasswordInput(attrs={
              'class': 'form-control form-control-lg',
              'placeholder': 'Password Confirmation'
        }),
    )

    class Meta:
        model = Cook
        fields = ('username', 'email', )

        widgets = {
            'username': forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            "placeholder": "Username"
        }),
            'email': forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Email'
              })
            }
