from django.shortcuts import render, redirect

from .models import Post
from .forms import PostForm

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('posts:create')
    else:
        # post를 작성하는 form을 보여줌
        form = PostForm()
        return render(request, 'instajs/create.html', {'form': form})
