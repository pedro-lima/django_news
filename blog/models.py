# *-* coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse

class Blog(models.Model):
    titulo = models.CharField(max_length=150)
    blogueiro = models.CharField(max_length=250)
    chave = models.SlugField(unique=True)
    email = models.EmailField(u'e-mail',blank=True)

    def get_absolute_url(self):
        return reverse('blog.views.listar_postagens_por_blog',
            kwargs = {'slug': self.chave}
        )

class Postagem(models.Model):
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(u'data de publicação')
    data_atualizacao = models.DateTimeField(u'data de atualização')
    referencia = models.URLField(blank=True)
    chave = models.SlugField(u'palavra chave', unique=True)
    blog = models.ForeignKey(Blog)

    def get_absolute_url(self):
        return reverse('blog.views.buscar_postagem_por_chave',
            kwargs = {'slug': self.chave}
        )



    #fotos

#class Imagem(models.Model):
