from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    def __unicode__(self):
        return u'%s' % (self.nome)

class Regiao(models.Model):
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.nome)
    
class Reporter(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __unicode__(self):
        return u'%s %s' % (self.nome, self.sobrenome)
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    subTitulo = models.CharField(max_length=255)    
    dataPublicacao = models.DateField()
    dataAtualizacao = models.DateField()
    texto = models.TextField()
    referencia = models.URLField(blank=True)
    regiao = models.ForeignKey(Regiao)
    categoria = models.ForeignKey(Categoria)
    reporter = models.ForeignKey(Reporter)
        
    def ___unicode__(self):
        return u'%s - %s' % (self.titulo, self.subTitulo)

class Comentario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    dataCriacao = models.DateField()
    comentario = models.TextField()
    aprovado = models.BooleanField()   
    noticia = models.ForeignKey(Noticia)
    
    def __unicode__(self):
        return u'%s - %s' % (self.email, self.noticia) 
#Imagens
#Videos
