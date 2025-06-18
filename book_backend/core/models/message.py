from django.db import models
from .userprofile import UserProfile
from .chatroom import ChatRoom

class Message(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    cloudinary_id = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_ai = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} in Room {self.room.id} at {self.timestamp}"