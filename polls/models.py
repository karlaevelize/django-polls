from django.db import models

# Create your models here.
class Question(models.Model):
  #required to give it a max_length argument, on db schema and validation
  question_text = models.CharField(max_length=200) 
  pub_date = models.DateTimeField('date published')

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

## IMPORTANT: To include the app in our project, 
# we need to add a reference to its configuration 
# class in the INSTALLED_APPS setting
