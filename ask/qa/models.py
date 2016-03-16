from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone

class Question(models.Model):
    title = models.CharField(max_length=127)
    text = models.TextField()
    added_at = models.DateTimeField(default=django.utils.timezone.now)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')
    def __unicode__(self):
        return self.text


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(default=django.utils.timezone.now)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.text
