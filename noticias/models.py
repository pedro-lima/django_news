# *-* coding:utf-8
from django.db import models
from datetime import datetime

class Categoria(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    chave = models.SlugField(u'palavra chave', unique=True)

    def __unicode__(self):
        return u'%s' % (self.nome)

    class Meta:
        ordering = ['nome']

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    sub_titulo = models.CharField(max_length=255)
    data_publicacao = models.DateTimeField(u'data de publicação',default=datetime.now)
    data_atualizacao = models.DateTimeField(u'data de atualização')
    texto = models.TextField()
    referencia = models.URLField(blank=True)
    chave = models.SlugField(u'palavra chave', unique=True)
    categorias = models.ManyToManyField(Categoria,verbose_name='categorias')

    def __unicode__(self):
        return u'%s - %s' % (self.titulo, self.sub_titulo)

    def get_absolute_url(self):
        return '/noticia/%d/' %(self.id)

    class Meta:
        ordering = ['-data_publicacao']
        verbose_name = 'notícia'
        verbose_name_plural = 'notícias'
        get_latest_by = '-data_publicacao'

#class Comentario(models.Model):
#    nome = models.CharField(max_length=250)
#    email = models.EmailField()
#    data = models.DateTimeField()
#    mensagem = models.TextField()
#    aprovado = models.BooleanField()
#    noticia = models.ForeignKey(Noticia)
#
#    def __unicode__(self):
#        return u'%s - %s' % (self.email, self.noticia)
#
#    class Meta:
#        ordering = ['-data']
#        get_latest_by = 'data'
#        verbose_name = 'comentário'
#        verbose_name_plural = 'comentários'

class Video(models.Model):
    titulo = models.CharField(u'título', max_length=150)
    url = models.URLField(u'link do vídeo')
    noticia = models.OneToOneField(Noticia)

    def __unicode__(self):
        return u'%s' % (self.titulo)

    class Meta:
        verbose_name = 'vídeo'
        verbose_name_plural = 'vídeos'


#Imagens
