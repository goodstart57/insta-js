from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    username = forms.CharField(
        label="username", # label: html에서 붙일 이름
        widget=forms.TextInput(attrs={
            'placeholder': "ID를 입력해주세요."
        })
    )
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput()
    )
    
    class Meta:
        model = User
        fields = ['username', 'password']
    
    
class UserForm(forms.ModelForm):
    username = forms.CharField(
        label="username", # label: html에서 붙일 이름
        widget=forms.TextInput(attrs={
            'placeholder': "ID를 입력해주세요."
        })
    )
    email = forms.EmailField(
        label="email", # label: html에서 붙일 이름
        widget=forms.TextInput(attrs={
            'placeholder': "Email을 id@email.com 형식에 맞게 입력해주세요."
        })
    )
    email = forms.EmailField(
        label="email", # label: html에서 붙일 이름
        widget=forms.TextInput(attrs={
            'placeholder': "Email을 id@email.com 형식에 맞게 입력해주세요."
        })
    )
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput()
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']