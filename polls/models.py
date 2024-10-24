import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    difficulty = models.PositiveSmallIntegerField()
    leetCode = models.BooleanField()

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.choice_text


class UserProfile(models.Model):
    user_name = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    age = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=200)
    questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.user_name