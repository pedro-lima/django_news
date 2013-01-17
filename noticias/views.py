from noticias.models import Noticia, Categoria
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template  import RequestContext
from noticias.forms import BuscaForm
from django.db.models import Q
from django_news.util import gerenciar_paginacao

#OK
def listar_noticias(request):
    noticias_list = Noticia.objects.all()
    noticias = gerenciar_paginacao(request, noticias_list)

    return render_to_response('listagem_noticias.html',
        {'noticias':noticias},context_instance=RequestContext(request))

#OK
def listar_noticias_por_categoria(request,slug):
    noticias_list = Noticia.objects.filter(categorias__chave=slug)
    noticias = gerenciar_paginacao(request, noticias_list)

    return render_to_response('listagem_noticias.html',
        {'noticias':noticias},context_instance=RequestContext(request))

#OK
def realizar_busca_noticias(request):
    form = BuscaForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        noticias_list = Noticia.objects.filter( Q(titulo__icontains=data['termo']) |
            Q(sub_titulo__icontains=data['termo']))
        noticias = gerenciar_paginacao(request, noticias_list)
    else:
        noticias = None
    return render_to_response('buscar_noticias.html',
        locals(),context_instance=RequestContext(request))

#OK
def buscar_noticia_por_chave(request,slug):
    noticia = get_object_or_404(Noticia,chave=slug)
    return render_to_response('noticia_detalhe.html',locals(),
        context_instance=RequestContext(request))



from datetime import datetime
def teste_cookie(request,response):
    if "teste_cookie" not in request.COOKIES:
        response.set_cookie('teste_cookie','novo', max_age=60)
    else:
        response.set_cookie('teste_cookie',datetime.now())

def teste_session(request):
    if "teste_session" in request.session:
        request.session['teste_session'] = "novo"
    else:
        request.session['teste_session'] = datetime.now()   
