from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST  # POST외의 요청 무시
from django.contrib.auth.decorators import login_required  # 로그인 되어있을 때만 허용

from .models import Post
from .forms import PostForm

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('posts:list')
    else:
        # post를 작성하는 form을 보여줌
        form = PostForm()
        return render(request, 'instajs/create.html', {'form': form})


def list(request):
    # 모든 포스트를 보여준다.
    return render(request, 'instajs/list.html', {'posts': Post.objects.all()})


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.user == request.user:
        post.delete()
    return redirect('posts:list')
    


def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if post.user == request.user and form.is_valid():
            form.save()
        return redirect('posts:list')
    else:
        form = PostForm(instance=post)
        return render(request, 'instajs/update.html', {'form': form})


@login_required
def like(request, post_id):
    """유저가 게시물을 좋아요하는 기능
    1. like를 추가할 포스트를 가져옴
    2. 유저가 해당 포스트를 이미 like 했다면,
            like 제거
       아니라면,
            like 추가
    """
    post = get_object_or_404(Post, id=post_id)
    
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    
    return redirect('posts:list')
        