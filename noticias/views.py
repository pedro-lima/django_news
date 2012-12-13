from django.http import HttpResponse, Http404
from noticias.models import Noticia, Regiao, Categoria
from django.shortcuts import render_to_response
import datetime

def time_add(request,num):
    #try:
    #    num = int(num)
    #except ValueError:
    #    raise Http404()
    time = datetime.datetime.now() + datetime.timedelta(hours=num) 
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" %(time,num)     
    return HttpResponse(html)

def buscar_noticias_por_categoria(request,categoria):
    noticias = Noticia.objects.filter(categoria__chave=categoria)
    return render_to_response('buscar_noticias_por_categoria.html',locals())

def buscar_noticias_por_regiao(request,regiao):    
    noticias = Noticia.objects.filter(regiao__chave=regiao)
    return render_to_response('buscar_noticias_por_regiao.html',locals())

def buscar_noticia_por_chave(request,noticia):
    try:
        noticia = Noticia.objects.get(chave=noticia)
    except Noticia.DoesNotExist:
        noticia = None    
    return render_to_response('buscar_noticia_por_chave.html',locals())

def buscar_ultimas_noticias(request):
    noticias = Noticia.objects.all()[0:20]
    return render_to_response('buscar_ultimas_noticias.html',locals())

def buscar_noticia_pelo_nome(request,noticia):
    noticias = Noticia.objects.filter(nome__contais=noticia)
    return render_to_response('buscar_noticia_pelo_nome.html',locals())

#def cadastrar_comentario(request):