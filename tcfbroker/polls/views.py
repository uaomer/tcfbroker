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
    all_profile = Profile.objects.order_by('-caiq_score') 
    template = loader.get_template('polls/profile.html')
    context = {
        'all_profile': all_profile,
    }
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
    Profile.objects.filter(id=profile_id).update(caiq_score=trust_e) 
    
    return HttpResponse(template.render(context, request))
 
#def import_sheet(request, profile_id):
#     if request.method == "POST":
#         form = UploadFileForm(request.POST,
#                               request.FILES)
#         
#           
#         if form.is_valid():
#             input_excel = request.FILES['file']
#             book = xlrd.open_workbook(file_contents=input_excel.read())
#             xl_sheet = book.sheet_by_index(0)
#         
#             num_rows = xl_sheet.nrows   # Number of rows
#             num_cols = xl_sheet.ncols   # Number of columns
#         
#             myrow = xl_sheet.row(row)
#             
#         mycell = xl_sheet.cell(1,2)
#             
#         for row_idx in range(0, num_rows):    # Iterate through rows
# #                 for col_idx in range(0, num_cols):  # Iterate through columns
# #                     cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
# #             
#         #   return render_to_response('polls/test.html', {'cell_obj': cell_obj})
#             context = {
#                     'xl_sheet': xl_sheet,
#                     'myrow': myrow,
#                     'mycell': mycell,
#                 }
# 
#             template = loader.get_template('polls/test.html')
#             
#             return HttpResponse(template.render(context, request))  
#            # return HttpResponse('Sheet name: %s, row: %s, Cell: %s' %(xl_sheet.name, myrow, mycell))
# #             
# #             for row_idx in range(0, num_rows):    # Iterate through rows
# #                 for col_idx in range(0, num_cols):  # Iterate through columns
# #                     cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
# #             
# #             context = {
# #                     
# #                     'all_results': all_resources
# #                     }
# #             
# #             return HttpResponse ('Rows: [%s] Columns: [%s]' % (num_rows, num_cols))
# #             
#             #return HttpResponse("OK")
#         
#         #return HttpResponse('Sheet name: %s' % xl_sheet.name)
#        
#         else:
#             return HttpResponseBadRequest()
#     else:
#         form = UploadFileForm()
#     return render(request, 'polls/upload_form.html', {'form': form})    


# 
# def line(request):
#     ds = DataPool(
#        series=
#         [{'options': {
#             'source': MonthlyWeatherByCity.objects.all()},
#           'terms': [
#             'month',
#             'houston_temp', 
#             'boston_temp']}
#          ])
# 
#     cht = Chart(
#             datasource = ds, 
#             series_options = 
#               [{'options':{
#                   'type': 'line',
#                   'stacking': False},
#                 'terms':{
#                   'month': [
#                     'boston_temp',
#                     'houston_temp']
#                   }}],
#             chart_options = 
#               {'title': {
#                    'text': 'Weather Data of Boston and Houston'},
#                'xAxis': {
#                     'title': {
#                        'text': 'Month number'}}})
# 
#     return render_to_response('polls/chart.htm', {'cht':cht})
#     