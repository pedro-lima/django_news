# *-* coding:utf-8
from django import template
from blog.models import Blog

register = template.Library()

class ListagemBlogsNode(template.Node):
    def __init__(self,blogs):
        self.blogs = blogs

    def render(self,context):
        context['blog_list'] = self.blogs
        return ''       

@register.tag
def listar_blogs(parser,token):
    return ListagemBlogsNode(Blog.objects.all())
