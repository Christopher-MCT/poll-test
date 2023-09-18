from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now
    
    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True, 
        ordering='pub_date', 
        description='Published recently?', 

    )
    def was_pulished_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    
    def __str__(self):
        return self.choice_text
    


