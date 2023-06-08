from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from gro_drf.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    Lists all profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrive or update your profile if owner.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsOwnerOrReadOnly]