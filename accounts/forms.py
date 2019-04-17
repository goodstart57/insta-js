from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

from . import models

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('nickname', 'description',)