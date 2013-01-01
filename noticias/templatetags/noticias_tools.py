from django import template
from noticias.models import Noticia, Categoria

register = template.Library()

class ListagemCategoriasNode(template.Node):
    def __init__(self,categorias):
        self.categorias = categorias

    def render(self,context):
        html = []
        if self.categorias:
            for i, cat in enumerate(self.categorias):
                if i==0:
                    html.append("<li class='first'><a href='%s'>%s</a></li>" %(cat.get_absolute_url(),cat.nome))
                else:
                    html.append("<li><a href='%s'>%s</a></li>" %(cat.get_absolute_url(),cat.nome))
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
                   html.append("<li class='first'><span class='date'>%s</span><a href='%s'>%s</a></li>" %(noti.get_short_date(),
                       noti.get_absolute_url(), noti.titulo))
               else:
                   html.append("<li><span class='date'>%s</span><a href='%s'>%s</a></li>" %(noti.get_short_date(),
                       noti.get_absolute_url(),noti.titulo))
        else:
            html.append("<li class='first'>Sem noticias cadastradas</li>")
        return ''.join(html)

@register.tag
def listar_categorias(parser,token):
    return ListagemCategoriasNode(Categoria.objects.all())

@register.tag
def listar_noticias(parser,token):
    return ListagemNoticiasNode(Noticia.objects.all()[0:5])

#http://djangosnippets.org/snippets/1919/
