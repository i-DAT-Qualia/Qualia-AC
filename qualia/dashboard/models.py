from django.db import models

class FrontPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.CharField(max_length=250,blank=True,null=True)

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
