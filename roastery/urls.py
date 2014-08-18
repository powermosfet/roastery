from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from roast.api import *
from inventory.api import *

v1_api = Api(api_name = 'v1')
v1_api.register(BatchResource())
v1_api.register(RoastpointResource())
v1_api.register(EventResource())

v1_api.register(VarietyResource())

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('roast.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounting/', include('accounting.urls')),
    url(r'^roast/', include('roast.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^sales/', include('sales.urls')),
    url(r'^api/', include(v1_api.urls)),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
