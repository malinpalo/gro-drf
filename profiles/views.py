from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from gro_drf.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    Lists all profiles
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-date_created')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__date_created',
        'owner__followed__date_created',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrive or update your profile if owner.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-date_created')
    permission_classes = [IsOwnerOrReadOnly]