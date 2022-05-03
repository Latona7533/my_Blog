from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment',on_delete=models.CASCADE)
    username = models.CharField(max_length=15)
    text = models.TextField(null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

