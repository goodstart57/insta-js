from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    get_user_model,
    update_session_auth_hash,
)
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import (
    CustomUserChangeForm,
    CustomUserCreationForm,
    ProfileForm,
)
from .models import Profile


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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            auth_login(request, user)
        return redirect("posts:list")
    else:  # GET: 유저 정보 입력
        return render(request, 'accounts/signup.html', {'form': CustomUserCreationForm()})


def people(request, username):
    # 사용자에 대한 정보
    # 1. django.contrib.auth.get_user_model()
    # 2. django.conf.settings.AUTH_USER
    # 3. django.contrib.auth.models.User (X)
    person = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/people.html', {'people': person})
    

@login_required
def update(request):
    """회원 정보 변경"""
    if request.method == "POST":
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        
        profile = get_object_or_404(Profile, user=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        
        if user_change_form.is_valid():
            user = user_change_form.save()
        else:
            user = request.user
        
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
        
        return redirect("people", user.username)
    else:  # GET
        user_change_form = CustomUserChangeForm(instance=request.user)
        
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)
        
        return render(request, 'accounts/update.html', {
            'user_change_form': user_change_form,
            'profile_form': profile_form,
        })


@login_required
def delete(request):
    """회원 탈퇴"""
    if request.method == "POST":
        request.user.delete()
        return redirect("accounts:signup")
    else:
        return render(request, 'accounts/delete.html')


@login_required
def password(request):
    """비밀번호 변경"""
    if request.method == "POST":
        password_chage_form = PasswordChangeForm(request.user, request.POST)
        if password_chage_form.is_valid():
            password_chage_form.save()
            update_session_auth_hash(request, request.user)
        return redirect("people", request.user)
    else:
        password_chage_form = PasswordChangeForm(request.user)
        return render(request, 'accounts/password.html', {'password_chage_form': password_chage_form})


@login_required
@require_POST
def follow(request, user_id):
    person = get_object_or_404(get_user_model(), pk=user_id)
    
    if person == request.user:
        return redirect('people', person.username)    
    
    # 만약 현재 유저가 해당 유저를 이미 팔로우 하고 있었으면,
    #  -> 팔로우 취소
    # 아니면
    #  -> 팔로우
    if person in request.user.followings.all():
        request.user.followings.remove(person)
    else:
        request.user.followings.add(person)
    
    return redirect('people', person.username)
        
    