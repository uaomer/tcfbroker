from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from ._compact import JsonResponse 
from django.urls import reverse
#from django.views import generic
from django.template import loader
from django import forms
import django_excel as excel
import xlrd
from chartit import DataPool, Chart




from .models import Choice, Question, Profile, Resource, Assessment, MonthlyWeatherByCity
from django.template.context_processors import request
from pyexcel.sheets import row

#from tcfbroker.polls.models import Assessment


#class UploadFileForm(forms.Form):
#    file = forms.FileField()


def index(request):
    latest_question_list = Question.objects.order_by('id')
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
  
def profile(request):
    all_profile = Profile.objects.order_by('-caiq_escore') 
    template = loader.get_template('polls/profile.html')
    
    ds = DataPool(
       series=
        [{'options': {
            'source': Profile.objects.all()},
          'terms': [
            'name_text',
             
            'caiq_escore']}
         ])
 
    cht = Chart(
            datasource = ds, 
            series_options = 
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'name_text': [
                    'caiq_escore'
                    ]
                  }}],
            chart_options = 
              {'title': {
                   'text': 'Trust Rating of CSPs in Federation'},
               'xAxis': {
                    'title': {
                       'text': 'Cloud Service Providers'}}})

    context = {
        'all_profile': all_profile,
        'chart': cht
    }
    

   # return render_to_response('chartit/chart.html', {'weatherchart':cht})
    
    return HttpResponse(template.render(context, request))


def cspdetail(request, profile_id):
   
    select_profile = get_object_or_404(Profile, pk=profile_id)
   # all_resources = Resource.objects.filter(cloud=profile_id)
   # iaas_resources = Resource.objects.filter(cloud=profile_id).filter(rtype='IaaS').count()
   # paas_resources = Resource.objects.filter(cloud=profile_id).filter(rtype='PaaS').count()
   # saas_resources = Resource.objects.filter(cloud=profile_id).filter(rtype='SaaS').count()
   
    total_assessment = Assessment.objects.filter(acloud=profile_id).count()

    yes_assessment = Assessment.objects.filter(acloud=profile_id).filter(ayes='X').count() # Answered Yes 
    no_assessment= Assessment.objects.filter(acloud=profile_id).filter(ano='X').count() # Answered No 
    na_assessment = Assessment.objects.filter(acloud=profile_id).filter(ana='X').count() # Answered Not Application 
        
    una_assessment =  total_assessment - (yes_assessment + no_assessment + na_assessment) # Never Answered  
    ta_assessment = total_assessment - na_assessment # total applicable 
    
    trust_t= yes_assessment / (yes_assessment + no_assessment) 
    temp1= ta_assessment * (yes_assessment + no_assessment)
    temp2 = 2*(ta_assessment - (yes_assessment+no_assessment))
       
    trust_c= temp1 / (temp2+temp1)
    
    trust_f= 0.99
    trust_e = trust_t * trust_c + (1-trust_c)*trust_f
    
    trust_b = yes_assessment / (yes_assessment + no_assessment + 2)
    trust_d = no_assessment / (yes_assessment + no_assessment + 2)
    trust_u = 2 / (yes_assessment + no_assessment + 2)
    
    
    template = loader.get_template('polls/cspdetail.html')
   
    context = {
    'select_profile': select_profile,
 #   'all_resources': all_resources,
  #  'iaas_resources': iaas_resources,
   # 'paas_resources': paas_resources,
    #'saas_resources': saas_resources, 
    'total_assessment': total_assessment,
    'yes_assessment': yes_assessment,
    'no_assessment': no_assessment,
    'na_assessment': na_assessment,
    'una_assessment': una_assessment,
    'ta_assessment': ta_assessment,
    'trust_t':trust_t, 
    'trust_c':trust_c,
    'trust_f':trust_f,
    'trust_e':trust_e,
    
    'trust_b':trust_b, 
    'trust_d':trust_d,
    'trust_u':trust_u,  
 #   'ais_assessment':ais_assessment,
    }
        
#        >>> Publisher.objects.filter(id=1).update(name='Apress Publishing')
    Profile.objects.filter(id=profile_id).update(caiq_t=trust_t, 
                                                 caiq_c=trust_c, 
                                                 caiq_escore=trust_e, 
                                                 caiq_f=trust_f,
                                                 caiq_b=trust_b,  
                                                 caiq_d=trust_d, 
                                                 caiq_u=trust_u ) 
    
    return HttpResponse(template.render(context, request))