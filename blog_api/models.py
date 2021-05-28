from django.db import models


# Create your models here.
class BlogPost(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tittle = models.CharField(max_length=100, blank=True, default="")
    body = models.TextField(blank=True, default="")
    owner = models.ForeignKey("auth.User", related_name="posts", on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('BlogPost', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
