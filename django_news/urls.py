from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from noticias.feed import UltimasNoticias
from noticias.sitemap import NoticiaSitemap
from blog.models import Postagem
import settings

admin.autodiscover()

info_dict = {
  'queryset'   : Postagem.objects.all(),
  'date_field' : 'data_atualizacao',

}

sitemaps = {
    'flatpage' : FlatPageSitemap,
    'blog'     : GenericSitemap(info_dict, priority = 0.6),
    'noticia'  : NoticiaSitemap
}

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^extras/',include('extras.urls')),
    (r'^contato/$','django_news.views.enviar_mensagem'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^noticia/(?P<slug>.*)/$','noticias.views.buscar_noticia_por_chave'),
    (r'^blog/(?P<slug>.*)/$','blog.views.listar_postagens_por_blog'),
    (r'^postagem/(?P<slug>.*)/$','blog.views.buscar_postagem_por_chave'),
    (r'^busca/','noticias.views.realizar_busca_noticias'),
    (r'^$','noticias.views.listar_noticias'),
    (r'^categoria/(?P<slug>.*)/$','noticias.views.listar_noticias_por_categoria'),

    #Medias
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  {'document_root': settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),

    #RSS
    (r'^rss/$', UltimasNoticias()),

    #Sitemap
    #(r'sitemap\.xml$','django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'sitemap\.xml$','django.contrib.sitemaps.views.index', {'sitemaps': sitemaps}),
    (r'sitemap-(?P<section>.+)\.xml$','django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    #CKEDITOR
    (r'^ckeditor/', include('ckeditor.urls')),

    (r'^i18n/', include('django.conf.urls.i18n')),

)

if(settings.DEBUG):
    urlpatterns += patterns('',

)
