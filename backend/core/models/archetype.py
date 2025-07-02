from django.db import models

class Archetype(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    genres = models.JSONField()

    def __str__(self):
        return self.name
 