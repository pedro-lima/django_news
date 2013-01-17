from django import template
from noticias.models import Noticia, Categoria

register = template.Library()

class ListagemCategoriasNode(template.Node):
    def __init__(self,categorias):
        self.categorias = categorias

    def render(self,context):        
        context['categorias_list'] = self.categorias
        return ''

class ListagemNoticiasNode(template.Node):
    def __init__(self,noticias):
        self.noticias = noticias

    def render(self,context):
        context['noticias_list'] = self.noticias
        return ''       

@register.tag
def listar_categorias(parser,token):
    return ListagemCategoriasNode(Categoria.objects.all())

@register.tag
def listar_noticias(parser,token):
    return ListagemNoticiasNode(Noticia.objects.all()[0:5])

#http://djangosnippets.org/snippets/1919/
