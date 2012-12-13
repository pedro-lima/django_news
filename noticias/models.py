# *-* coding:utf-8
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    chave = models.SlugField(u'palavra chave', unique=True)

    def __unicode__(self):
        return u'%s' % (self.nome)

    class Meta:
        ordering = ['nome']

class Regiao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    chave = models.SlugField(u'palavra chave', unique=True)

    def __unicode__(self):
        return u'%s' % (self.nome)

    class Meta:
        ordering = ['nome']
        verbose_name= 'região'
        verbose_name_plural = 'regiões'

class Reporter(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(u'e-mail',blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.nome, self.sobrenome)

    class Meta:
        ordering = ['nome']
        verbose_name = 'repórter'
        verbose_name_plural = 'repórteres'

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    sub_titulo = models.CharField(max_length=255)
    data_publicacao = models.DateTimeField(u'data de publicação')
    data_atualizacao = models.DateTimeField(u'data de atualização')
    texto = models.TextField()
    referencia = models.URLField(blank=True)
    chave = models.SlugField(u'palavra chave', unique=True)
    regiao = models.ForeignKey(Regiao,verbose_name=u'região')
    categorias = models.ManyToManyField(Categoria,verbose_name='categorias')
    reporter = models.ForeignKey(Reporter,blank=True,null=True)

    def __unicode__(self):
        return u'%s - %s' % (self.titulo, self.sub_titulo)

    class Meta:
        ordering = ['titulo']
        verbose_name = 'notícia'
        verbose_name_plural = 'notícias'
        get_latest_by = 'data_publicacao'

class Comentario(models.Model):
    nome = models.TextField()
    email = models.EmailField()
    data = models.DateTimeField()
    comentario = models.TextField()
    aprovado = models.BooleanField()
    noticia = models.ForeignKey(Noticia)

    def __unicode__(self):
        return u'%s - %s' % (self.email, self.noticia)

    class Meta:
        ordering = ['-data']
        get_latest_by = 'data'
        verbose_name = 'comentário'
        verbose_name_plural = 'comentários'

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
