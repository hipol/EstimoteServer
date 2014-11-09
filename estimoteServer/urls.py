from django.conf.urls import patterns, include, url
from django.contrib import admin
from estimote import views as estimote_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'estimoteServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^datapoints/', estimote_views.datapoint_list),
)
