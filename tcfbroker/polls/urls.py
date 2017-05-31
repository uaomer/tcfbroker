'''
Created on Apr 3, 2017

@author: Peterpan
'''
from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
 #   url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
  #  url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
  #  url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^profile/$', views.profile, name='profile'),
   # url(r'^csp_list/$', views.profile, name='csp_list'),  
    url(r'^profile/(?P<profile_id>[0-9]+)/$', views.cspdetail, name='cspdetail'),
  #  url(r'^import_sheet/(?P<profile_id>[0-9]+)/$', views.import_sheet, name="import_sheet"),
  #  url(r'^chart/$', views.line, name='cht')
]