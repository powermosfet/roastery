from django.conf.urls import patterns, include, url

from sales.views import OutstandingOrders

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('roast.urls')),
    url(r'^roast/', include('roast.urls')),
    url(r'^outstanding_orders/$', OutstandingOrders.as_view() ),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
