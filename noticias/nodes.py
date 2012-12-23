# *-* coding:utf-8
from django import template
from noticias.models import Noticia, Categoria

class ListagemCategoriasNode(template.Node):
    def __init__(self,categorias):
        self.categorias = categorias

    def render(self,context):
        html = []
        if self.categorias:
            for i, cat in enumerate(self.categorias):
                if i==0:
                    html.append("<li class='first'><a href='/%s'>%s</a></li>" %(cat.get_friendly_url(),cat.nome))
                else:
                    html.append("<li><a href='/%s'>%s</a></li>" %(cat.get_friendly_url(),cat.nome))
        else:
            html.append("<li class='first'>Sem categorias cadastradas</li>")
        return ''.join(html)

class ListagemNoticiasNode(template.Node):
    def __init__(self,noticias):
        self.noticias = noticias

    def render(self,context):
        html = []
        if self.noticias:
            for i,noti in enumerate(self.noticias):
               if i==0:
                   html.append("<li class='first'><span class='date'>%s</span><a href='/%s'>%s</a></li>" %(noti.get_short_date(),
                       noti.get_friendly_url(), noti.titulo))
               else:
                   html.append("<li><span class='date'>%s</span><a href='/%s'>%s</a></li>" %(noti.get_short_date(),
                       noti.get_friendly_url(),noti.titulo))
        else:
            html.append("<li class='first'>Sem noticias cadastradas</li>")
        return ''.join(html)
