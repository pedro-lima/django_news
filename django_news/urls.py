from django.conf.urls import patterns, include, url
from django.contrib import admin
from noticias.feed import UltimasNoticias
import settings

admin.autodiscover()

feeds = {
    'ultimos': UltimasNoticias,
}

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^rss/$', UltimasNoticias()),
    (r'noticia/(?P<noticia_id>\d+)/$','noticias.views.buscar_noticia_por_id'),

    #Medias
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  {'document_root': settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),	
)

if(settings.DEBUG):
    urlpatterns += patterns('',
  
)
