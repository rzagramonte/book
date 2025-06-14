from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ColorType(models.Model):
    name = models.CharField(max_length=50)
    genres = models.JSONField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    color_type = models.ForeignKey(ColorType, on_delete=models.SET_NULL, null=True, blank=True) # from your quiz logic
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.display_name or self.user.username