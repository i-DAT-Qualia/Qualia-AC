from artcasting.models import *
from rest_framework import serializers
from rest_framework_gis.serializers import GeometryField


class UserSerializer(serializers.HyperlinkedModelSerializer):
        #postcode_geolocation = GeometryField()

        class Meta:
            model = User
            exclude = ('postcode_geolocation',)

class CastSerializer(serializers.HyperlinkedModelSerializer):
        destination = GeometryField()
        origin = GeometryField()
        tags = serializers.ListField()
        class Meta:
            model = Cast

class ArtworkSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Artwork
