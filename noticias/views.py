from django.http import HttpResponse, Http404
from noticias.models import Noticia, Categoria
from django.shortcuts import render_to_response, get_object_or_404
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

def buscar_noticia_por_id(request,noticia_id):
    noticia = get_object_or_404(Noticia,id=noticia_id)
    return render_to_response('noticia_detalhe.html',locals(),
        context_instance=RequestContext(request))


def buscar_noticia_por_chave(request,noticia):
    noticia = get_object_or_404(Noticia,chave=noticia)
    return render_to_response('buscar_noticia_por_chave.html',locals(),
        context_instance=RequestContext(request))
