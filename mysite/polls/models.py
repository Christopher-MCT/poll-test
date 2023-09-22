import datetime

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone



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
    
class CreateQues(models.Model):
   question = models.ForeignKey(Question, on_delete=models.CASCADE, default='1')
   choice = models.ForeignKey(Choice, on_delete=models.CASCADE, default='1')
   completed = models.BooleanField(default=False)
   created_at = models.DateTimeField(auto_now_add=True)


#https://swapps.com/es/blog/trabajando-con-formularios-anidados-con-django/


#>>> from polls.models import Choice, Question  # Import the model classes we just wrote.
#
## No questions are in the system yet.
#>>> Question.objects.all()
#<QuerySet []>
#
## Create a new Question.
## Support for time zones is enabled in the default settings file, so
## Django expects a datetime with tzinfo for pub_date. Use timezone.now()
## instead of datetime.datetime.now() and it will do the right thing.
#>>> from django.utils import timezone
#>>> q = Question(question_text="What's new?", pub_date=timezone.now())
#
## Save the object into the database. You have to call save() explicitly.
#>>> q.save()
#
## Now it has an ID.
#>>> q.id
#1
#
## Access model field values via Python attributes.
#>>> q.question_text
#"What's new?"
#>>> q.pub_date
#datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=datetime.timezone.utc)
#
## Change values by changing the attributes, then calling save().
#>>> q.question_text = "What's up?"
#>>> q.save()
#
## objects.all() displays all the questions in the database.
#>>> Question.objects.all()
#<QuerySet [<Question: Question object (1)>]>
#