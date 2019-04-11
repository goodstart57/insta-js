from django.db import models
# from django.contrib.auth.models import User를 settings에서 불러와서 사용한다.
from django.conf import settings

class Post(models.Model):
    content = models.CharField(max_length=150)
    image = models.ImageField(blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    __str__ = __repr__ = lambda self: self.content
