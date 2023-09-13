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
    

"""
class CreatePoll(models.Model):
    question_text= models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    choice_text = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=200)  
    choice_text = models.CharField(max_length=200)
    public_date = models.DateField()

    day  = timezone.now()
    hour = timezone.now()
    #formatedHour = hour.strftime("%Y/%m/%d %H:%M:%S")
    formatedDay  = day.strftime("%Y/%m/%d")
    formatedHour = hour.strftime("%H:%M:%S")

    def was_published_recently(self):
        now =timezone.now()
        return now-datetime.timedelta(days = 1) <=self.pub_date<=now
    def __str__(self):
        return self.question_text
"""

class NewUser(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=   True)
    web = models.URLField(blank=True)

    def __str__(self):
        return self.usuario.username
    
@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        NewUser.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()