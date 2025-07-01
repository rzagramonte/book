from django.db import models
from .archetype import Archetype

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    cover_image_url = models.URLField()
    cover_image_cloudinary_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    archetype = models.ForeignKey(Archetype, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author}"