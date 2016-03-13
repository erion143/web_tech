from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=127)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')


class Answer(models.Model):
    test = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
