from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        "message": "I am pleased to welcome you to my Gro-drf API!"
    })