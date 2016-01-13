from artcasting.models import *
from rest_framework import serializers
from rest_framework_gis.serializers import GeometryField


class UserSerializer(serializers.HyperlinkedModelSerializer):
        postcode_geolocation = GeometryField()

        class Meta:
            model = User

class CastSerializer(serializers.HyperlinkedModelSerializer):
        destination = GeometryField()
        origin = GeometryField()
        class Meta:
            model = Cast
