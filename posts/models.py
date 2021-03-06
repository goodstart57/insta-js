from django.db import models
# from django.contrib.auth.models import User를 settings에서 불러와서 사용한다.
from django.conf import settings

class Post(models.Model):
    content = models.CharField(max_length=150)
    image = models.ImageField(blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts", blank=True)
    
    __str__ = __repr__ = lambda self: f"{self.id}) {self.content}"


class Comment(models.Model):
    content = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    __str__ = __repr__ = lambda self: f"{self.id}) {self.user} => {self.post.user}: {self.content[:30]}"