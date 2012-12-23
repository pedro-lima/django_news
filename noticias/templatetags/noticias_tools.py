from django import template
from noticias.models import Noticia, Categoria
from noticias.nodes  import ListagemCategoriasNode, ListagemNoticiasNode
from blog.nodes import ListagemBlogsNode
from blog.models import Blog

register = template.Library()

@register.tag
def listar_categorias(parser,token):
    return ListagemCategoriasNode(Categoria.objects.all())

@register.tag
def listar_noticias(parser,token):
    return ListagemNoticiasNode(Noticia.objects.all()[0:5])

@register.tag
def listar_blogs(parser,token):
    return ListagemBlogsNode(Blog.objects.all())

#http://djangosnippets.org/snippets/1919/
