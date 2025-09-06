from django.db import models

from .archetype import Archetype
from .question import Question


class AnswerOption(models.Model):
    question = models.ForeignKey(
        Question, related_name="options", on_delete=models.CASCADE
    )
    text = models.TextField()

    def __str__(self):
        return self.text[:60]


class AnswerWeight(models.Model):
    answer = models.ForeignKey(
        AnswerOption, related_name="weights", on_delete=models.CASCADE
    )
    archetype = models.ForeignKey(Archetype, on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.answer} → {self.archetype.name} +{self.weight}"
