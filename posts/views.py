from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from gro_drf.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    If logged in: list posts or create a post
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrive, edit or delete a post if owner.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
