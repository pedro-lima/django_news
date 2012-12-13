from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url('^hello/$','noticias.views.hello'),
    #url('^$','noticias.views.hello'),
    #(r'^now','noticias.views.current_time'),
    #(r'time/(\d{1,2})/$','noticias.views.time_add')
)
