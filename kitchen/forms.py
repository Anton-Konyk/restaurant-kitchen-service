from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UsernameField,
    PasswordResetForm,
    UserCreationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.utils.translation import gettext_lazy as _

from kitchen.models import Cook


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Username"}
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Password"}
        ),
    )


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Old Password",
            }
        ),
        label="New Password",
    )
    new_password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "New Password",
            }
        ),
        label="New Password",
    )
    new_password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Confirm New Password",
            }
        ),
        label="Confirm New Password",
    )


class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "New Password",
            }
        ),
        label="New Password",
    )
    new_password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Confirm New Password",
            }
        ),
        label="Confirm New Password",
    )


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Email"}
        )
    )


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Password"}
        ),
    )
    password2 = forms.CharField(
        label=_("Password Confirmation"),
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Password Confirmation",
            }
        ),
    )

    class Meta:
        model = Cook
        fields = (
            "username",
            "email",
        )

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Username",
                }
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control form-control-lg", "placeholder": "Email"}
            ),
        }


class IngredientSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "🔎 Search by name"}),
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "🔎 Search by name"}),
    )
