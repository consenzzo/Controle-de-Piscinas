from django.db import models

class ProblemaComum(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    causas = models.TextField()
    solucoes = models.TextField()

    def __str__(self):
        return self.titulo
