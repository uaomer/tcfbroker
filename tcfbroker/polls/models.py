
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone
from django.template.defaultfilters import default
from _overlapped import NULL
#from unittest.util import _MAX_LENGTH

@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
   
    id = models.CharField(max_length=50, primary_key=True, default=NULL)
    question_text = models.CharField(max_length=300)
    q_phy = models.CharField(max_length=10, default=NULL) 
    q_net = models.CharField(max_length=10, default=NULL)
    q_comp = models.CharField(max_length=10, default=NULL)
    q_sto = models.CharField(max_length=10, default=NULL)
    q_app = models.CharField(max_length=10, default=NULL)
    q_data = models.CharField(max_length=10, default=NULL)
        
    def __str__(self):
        return self.question_text
   
class Choice(models.Model):
    # ...
    choice_text = models.CharField(max_length=50)
    
    def __str__(self):
        return self.choice_text

class Profile(models.Model):
    # ...
    name_text = models.CharField(max_length=200)
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
        return self.rpub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.rname
    

class Assessment(models.Model): 
    acloud = models.ForeignKey(Profile, on_delete=models.CASCADE, default=NULL)
    aquestion= models.ForeignKey(Question, on_delete=models.CASCADE)    
    ayes = models.CharField(max_length=10, null=True, blank=True)
    ano = models.CharField(max_length=10, null=True, blank=True)
    ana = models.CharField(max_length=10, null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    #def __str__(self):
    #    return self.rname
    
    
    
class MonthlyWeatherByCity(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)    