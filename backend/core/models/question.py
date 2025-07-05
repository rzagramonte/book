from django.db import models

class Question(models.Model):
    prompt = models.TextField()

    def __str__(self):
        return self.prompt[:60]