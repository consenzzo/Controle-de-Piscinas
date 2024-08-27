from django.db import models
from monitoramento.models import Medicao

class ParametrosTratamento(models.Model):
    parametro = models.CharField(max_length=100)
    valor_minimo = models.DecimalField(max_digits=4, decimal_places=2)
    valor_maximo = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.parametro} (Min: {self.valor_minimo}, Max: {self.valor_maximo})"


class RecomendacaoTratamento(models.Model):
    medicao = models.OneToOneField(Medicao, on_delete=models.CASCADE, related_name='recomendacao')
    recomendacoes = models.TextField()

    def __str__(self):
        return f"Recomendações para Medição {self.medicao.id}"