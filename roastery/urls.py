from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('roast.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounting/', include('accounting.urls')),
    url(r'^roast/', include('roast.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^sales/', include('sales.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
