
from django.db import models

class ColorType(models.Model):
    name = models.CharField(max_length=50)
    genres = models.JSONField()

    def __str__(self):
        return self.name
 