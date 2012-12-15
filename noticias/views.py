from django.http import HttpResponse, Http404
from noticias.models import Noticia, Categoria
from django.shortcuts import render_to_response, get_object_or_404
from django.template  import RequestContext
import datetime

def myhttp(request):
    #res =  "%s%s - %s" %(request.get_host(),request.get_full_path(),request.is_secure())
    #res = request.META.get('HTTP_USER_AGENT',None)
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><th>%s</th><td>%s</td</tr>' %(k,v))
    return HttpResponse('<table>%s</table>' %(html))

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        res = Reporter.objects.filter(nome__icontains=q)
        return render_to_response('search_results.html',{'res':res,'query':q})
    else:
        return HttpResponse('Please submit a search term.')


#==============================================================================================

#OK
def buscar_noticia_por_id(request,noticia_id):
    noticia = get_object_or_404(Noticia,id=noticia_id)
    return render_to_response('noticia_detalhe.html',locals(),context_instance=RequestContext(request))


def buscar_noticia_por_chave(request,noticia):
    try:
        noticia = Noticia.objects.get(chave=noticia)
        form = ComentarioForm()
        form['noticia'] = noticia.id
    except Noticia.DoesNotExist:
        noticia = None
    return render_to_response('buscar_noticia_por_chave.html',locals())

def buscar_ultimas_noticias(request):
    noticias = Noticia.objects.all()[0:20]
    return render_to_response('buscar_ultimas_noticias.html',locals())

def procurar_noticias(request):
    form = ComentarioForm(request.GET)
    if form.is_valid():
       cd = form.cleaned_data
       noticias = Noticia.objects.filter(nome__contais=cd['termo'])
    else:
        form = ComentarioForm()
    return render_to_response('resultado_busca_noticias.html',locals())
