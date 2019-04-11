from django.db import models

class Post(models.Model):
    content = models.CharField(max_length=150)
    image = models.ImageField(blank=True)
    
    __str__ = __repr__ = lambda self: self.content
