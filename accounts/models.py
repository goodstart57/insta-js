from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=48, blank=True)
    
    __str__ = lambda self: f"{self.id}) {self.user}({self.nickname}) -- {self.description[:30]}"