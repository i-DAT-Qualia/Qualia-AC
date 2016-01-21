from django.conf.urls import include, url

urlpatterns = [
    url(r'analytics/maps/casts/', 'dashboard.analytics.maps.cast_line_map'),
    url(r'', 'dashboard.views.dash_home_view'),
]
