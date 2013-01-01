from django.contrib.sitemaps import Sitemap
from models import Noticia

class NoticiaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Noticia.objects.all()

    def lastmod(self,obj):
        return obj.data_atualizacao
