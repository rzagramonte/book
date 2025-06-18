from django.db import models
from .colortype import ColorType

class ChatRoom(models.Model):
    color_type = models.ForeignKey(ColorType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    chat_pic_url = models.URLField(blank=True, null=True)
    chat_pic_cloudinary_id = models.CharField(max_length=255, blank=True, null=True)

    def current_user_count(self):
        return self.userprofile_set.count()

    def __str__(self):
        return f"{self.color_type.name} Room {self.id}"
