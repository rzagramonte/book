from django.db import models
from .colortype import ColorType

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    cover_image_url = models.URLField()
    description = models.TextField()
    color_type = models.ForeignKey(ColorType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author}"
