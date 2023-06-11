from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Model for the Posts, related to 'owner'.
    """
    post_filter_selections = [
        ('grow', 'Grow'),
        ('seeds', 'Seeds'),
        ('plant', 'Plant'),
        ('pots', 'Pots'),
        ('container', 'Container'),
        ('dig', 'Dig'),
        ('sole', 'Sole'),
        ('manure', 'Manure'),
        ('nutrition', 'Nutrition'),
        ('water', 'Water'),
        ('irrigation', 'Irrigation'),
        ('suspension', 'Suspension'),
        ('harvest', 'Harvest'),
        ('flowers', 'Flowers'),
        ('vegetables', 'Vegetables'),
        ('tree', 'Tree'),
        ('bushes', 'Bushes'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=245)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../gro_post_default.jgp', blank=True
    )
    post_filter = models.CharField(
        max_length=32, choices=post_filter_selections, default='normal'
    )

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.id} {self.title}'