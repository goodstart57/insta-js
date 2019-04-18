from django import forms
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
)
from django.contrib.auth import get_user_model

from . import models

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['nickname', 'description', 'image']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # fields를 그대로 쓰니까 정의하지 않고 그대로 사용해도 좋다.
        # fields = UserCreationForm.Meta.fields
        # fields = '__all__'