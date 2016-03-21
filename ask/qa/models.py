from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone

class Question(models.Model):
    title = models.CharField(max_length=127)
    text = models.TextField()
    added_at = models.DateTimeField(default=django.utils.timezone.now)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes_set')
    
    def __unicode__(self):
        return self.text

    def get_url(self):
        return '/question/%s/' % self.id


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(default=django.utils.timezone.now)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, blank=True, null=True)
    def __unicode__(self):
        return self.text

    def get_url(self):
        f = open('req.log', 'a')
        f.write('question_id = %s\n' % self.question_id)
        f.close()
        url = '/question/%s/' % self.question_id
        return url
