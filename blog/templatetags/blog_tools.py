# *-* coding:utf-8
from django import template
from blog.models import Blog
from blog.nodes import ListagemBlogsNode


def listar_blogs(parser,token):
    return ListagemBlogsNode(Blog.objects.all())
