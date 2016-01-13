from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
import uuid


class RootAC(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(blank=True)

class User(RootAC):
    postcode = models.CharField(max_length=250, blank=True)
    postcode_geolocation = models.PointField(blank=True, null=True)
    # TODO: age - requires ranges from Barker

    platform_choices = (
        ('I', 'iOS'),
        ('A', 'Android'),
        ('W', 'Web'),
    )

    platform = models.CharField(
        max_length=1,
        choices=platform_choices,
        blank=True
    )

    def __unicode__(self):
        return str(self.id)


class Cast(RootAC):
    destination = models.PointField(blank=True, null=True)
    origin = models.PointField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True)
    explanation = models.TextField(blank=True)
    speed = models.IntegerField(blank=True)
    has_arrived = models.NullBooleanField(default=None)
    is_a_recast = models.NullBooleanField(default=None)
    needs_review = models.NullBooleanField(default=None)
    arrival = models.DateTimeField(blank=True)

    def __unicode__(self):
        return str(self.id)
