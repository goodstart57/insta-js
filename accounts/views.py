from django.shortcuts import render, redirect
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout
)
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .forms import LoginForm

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # next가 정의되어 있으면 해당하는 url로 리다이렉트
            # 정의되어있지 않으면 posts:list로 리다이렉트
            return redirect(request.GET.get('next') or 'posts:list')
        return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})


def logout(request):
    auth_logout(request)
    return redirect('posts:list')


def signup(request):
    if request.method == "POST":  # 유저 등록
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
        return redirect("posts:list")
    else:  # GET: 유저 정보 입력
        return render(request, 'accounts/signup.html', {'form': UserCreationForm()})
    