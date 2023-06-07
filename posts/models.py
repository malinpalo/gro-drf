from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=245)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../gro_post_default.jgp', blank=True
    )

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.id} {self.title}'