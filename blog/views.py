from blog.models import Blog, Postagem
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template  import RequestContext
from django_news.util import gerenciar_paginacao

def listar_postagens_por_blog(request, slug):
    blog = get_object_or_404(Blog,chave=slug)
    posts = gerenciar_paginacao(request, blog.postagem_set.all())
    
    return render_to_response('listagem_post.html', locals(),
        context_instance=RequestContext(request))

def buscar_postagem_por_chave(request, slug):
    post = get_object_or_404(Postagem, chave=slug)
    return render_to_response('post_detalhe.html', locals(),
        context_instance=RequestContext(request))