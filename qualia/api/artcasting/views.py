from artcasting.models import *
from rest_framework import viewsets
from api.artcasting.serializers import *
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response


#class UserViewSet(viewsets.ReadOnlyModelViewSet):
class UserViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all user objects
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #@detail_route(methods=['post'])
    #def create_user(self, request, pk=None):


class CastViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all Casts
    """
    queryset = Cast.objects.all()
    serializer_class = CastSerializer


class ArtworkViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all Artworks
    """
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
