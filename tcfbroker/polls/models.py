
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone
from django.template.defaultfilters import default
#from unittest.util import _MAX_LENGTH

@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    # ...
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    # ...
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

class Profile(models.Model):
    # ...
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name_text = models.CharField(max_length=200)
    #models.CharField(_MAX_LENGTH=200)
    endpoint_text = models.CharField(max_length=200)
    meta_text = models.CharField(max_length=200)
    detail_info = models.TextField(default='')
    caiq_score= models.FloatField(default=0)
        
    def __str__(self):
        return self.name_text

class Resource(models.Model):
    
    cloud = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    rname = models.CharField(max_length=200)
    rtype = models.CharField(max_length=100)
    rvalue = models.CharField(max_length=100)
    runit = models.CharField(max_length=100)
    ravail = models.CharField(max_length=50)
    rpub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.rname
    
    
    
    
    
    
    
    
    