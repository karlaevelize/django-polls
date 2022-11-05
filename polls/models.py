import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
  #required to give it a max_length argument, on db schema and validation
  question_text = models.CharField(max_length=200) 
  pub_date = models.DateTimeField('date published')
  def __str__(self):
    return self.question_text
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
    return self.choice_text

## IMPORTANT: To include the app in our project, 
# we need to add a reference to its configuration 
# class in the INSTALLED_APPS setting
