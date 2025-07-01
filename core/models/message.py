from django.db import models
from .userprofile import UserProfile
from .group import Group

class Message(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    cloudinary_id = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_ai = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} in Room {self.group.id} at {self.timestamp}"