# *-* coding:utf-8
from django.db import models

class Blog(models.Model):
    titulo = models.CharField(max_length=150)
    blogueiro = models.CharField(max_length=250)
    chave = models.SlugField(unique=True)
    email = models.EmailField(u'e-mail',blank=True)

    def get_friendly_url(self):
        return '/blog/%s/' %(self.chave)

class Postagem(models.Model):
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(u'data de publicação')
    data_atualizacao = models.DateTimeField(u'data de atualização')
    referencia = models.URLField(blank=True)
    chave = models.SlugField(u'palavra chave', unique=True)
    blog = models.ForeignKey(Blog)
    #fotos

#class Imagem(models.Model):
