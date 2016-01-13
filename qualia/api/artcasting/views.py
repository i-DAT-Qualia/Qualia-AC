from artcasting.models import *
from rest_framework import viewsets
from api.artcasting.serializers import *


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of all user objects
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CastViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of all Cast objects
    """
    queryset = Cast.objects.all()
    serializer_class = CastSerializer
