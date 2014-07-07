from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

def lr_url(p, v, *args, **kwargs):
    return url(p, login_required(v), *args, **kwargs)
