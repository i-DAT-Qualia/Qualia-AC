from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver

from lib import PostCodeClient
from django.contrib.gis.geos import Point
import json

class RootAC(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(blank=True)

class User(RootAC):
    postcode = models.CharField(max_length=250, blank=True)
    postcode_geolocation = models.PointField(blank=True, null=True)
    # TODO: age - requires ranges from Barker

    age_choices = (
        ('A', "12 or under"),
        ('B', "13-15"),
        ('C', "16-17"),
        ('D', "18-20"),
        ('E', "21-23"),
        ('F', "24-25"),
        ('G', "26-35"),
        ('H', "36-45"),
        ('I', "46-55"),
        ('J', "56-74"),
        ('K', "75 or older"),
        ('N', "No Answer")
    )

    age = models.CharField(
        max_length=1,
        choices=age_choices,
        default="N"
    )


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

    encounters = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)


@receiver(post_save, sender=User)
def getPostcodeGeolocation(sender, instance, **kwargs):
    client = PostCodeClient()

    if not instance.postcode_geolocation:
        if instance.postcode:
            if json.loads(client.validatePostCode(instance.postcode))['result']:
                postcode = json.loads(client.getLookupPostCode(instance.postcode))
                instance.postcode_geolocation = Point(
                    postcode['result']['longitude'],
                    postcode['result']['latitude']
                )
                instance.save()


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

    sender = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return str(self.id)


class Artwork(RootAC):
    asset_name = models.CharField(max_length=250, unique=True)
    full_name = models.CharField(max_length=250, blank=True)
    artist_name = models.CharField(max_length=250, blank=True)
    year_produced = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.asset_name)
