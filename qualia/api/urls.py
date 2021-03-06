from django.conf.urls import url, include
from rest_framework import routers
from api.artcasting.views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'cast', CastViewSet)
router.register(r'artwork', ArtworkViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
]
