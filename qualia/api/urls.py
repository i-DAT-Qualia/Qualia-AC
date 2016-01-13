from django.conf.urls import url, include
from rest_framework import routers
from api.artcasting.views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'cast', CastViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
