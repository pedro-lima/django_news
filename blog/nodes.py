# *-* coding:utf-8
from django import template
from blog.models import Blog

class ListagemBlogsNode(template.Node):
    def __init__(self,blogs):
        self.blogs = blogs

    def render(self,context):
        html = []
        if self.blogs:
            for i,blog in enumerate(self.blogs):
                if i==0:
                    html.append("<li class='first'><a href='%s'>%s</a></li>" %(blog.get_friendly_url(),blog.titulo))
                else:
                    html.append("<li><a href='%s'>%s</a></li>" %(blog.get_friendly_url(),blog.titulo))

        else:
            html.append("<li class='first'>Sem blogs cadastrados</li>")
        return ''.join(html)
