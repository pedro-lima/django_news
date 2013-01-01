# *-* coding:utf-8
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from noticias.models import Noticia

class UltimasNoticias(Feed):
    title = "Ultimas notícias"
    link = "/"
    description = "Ultimas notícias cadastradas"

    def items(self):
        return Noticia.objects.all()

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.resumo
