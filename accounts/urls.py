from django.conf.urls import patterns, include, url
from django.views.generic import *

urlpatterns = patterns('',
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name = 'login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logout.html'}, name = 'logout'),
)
