from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Address


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "password1",
            "password2",
        ]



class CustomAthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "password",
        ]


class AddressCreationForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
