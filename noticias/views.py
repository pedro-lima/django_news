from django.http import HttpResponse, Http404
from noticias.models import Noticia, Categoria
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template  import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage

#OK
def listar_noticias(request):
    noticias_list = Noticia.objects.all()
    paginator = Paginator(noticias_list,1)

    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1

    try:
        noticias = paginator.page(page)
    except (InvalidPage, EmptyPage):
        noticias = paginator.page(paginator.num_pages)

    return render_to_response('listagem_noticias.html',
        {'noticias':noticias},context_instance=RequestContext(request))

def listar_noticias_por_categoria(request,slug):
    return redirect('http://localhost:8000/')

#OK
def buscar_noticia_por_chave(request,slug):
    noticia = get_object_or_404(Noticia,chave=slug)
    return render_to_response('noticia_detalhe.html',locals(),
        context_instance=RequestContext(request))
