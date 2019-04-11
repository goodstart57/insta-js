from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST  # POST외의 요청 무시

from .models import Post
from .forms import PostForm

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts:list')
    else:
        # post를 작성하는 form을 보여줌
        form = PostForm()
        return render(request, 'instajs/create.html', {'form': form})


def list(request):
    # 모든 포스트를 보여준다.
    return render(request, 'instajs/list.html', {'posts': Post.objects.all()})


@require_POST
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('posts:list')
    


def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts:list')
    else:
        form = PostForm(instance=post)
        return render(request, 'instajs/update.html', {'form': form})
