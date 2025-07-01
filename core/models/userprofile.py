from django.db import models
from django.contrib.auth.models import User
from .archetype import Archetype
from .group import Group

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True, null=True)
    profile_pic_url = models.URLField(blank=True, null=True)
    profile_pic_cloudinary_id = models.CharField(max_length=255, blank=True, null=True)
    primary_archetype = models.ForeignKey(Archetype, on_delete=models.SET_NULL, null=True, blank=True)
    archetype_rankings = models.JSONField(blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='members', blank=True)

    def __str__(self):
        return self.display_name or self.user.username