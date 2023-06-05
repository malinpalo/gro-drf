from rest_framework import serializers
from .models import Profile


class Meta:
    model = Profile
    fields = [
        'id', 'owner', 'date_created', 'date_updated', 'name',
        'description', 'name', 'image', 'city',
    ] 
