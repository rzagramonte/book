from django.db import models
from django.contrib.auth.models import User
from .colortype import ColorType
from .chatroom import ChatRoom

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True, null=True)
    profile_pic_url = models.URLField(blank=True, null=True)
    profile_pic_cloudinary_id = models.CharField(max_length=255, blank=True, null=True)
    primary_color = models.ForeignKey(ColorType, on_delete=models.SET_NULL, null=True, blank=True)
    color_rankings = models.JSONField(blank=True, null=True)
    chatrooms = models.ManyToManyField(ChatRoom, blank=True)

    def __str__(self):
        return self.display_name or self.user.username