from django.db import models
from core.models import Piscina

class Medicao(models.Model):
    piscina = models.ForeignKey(Piscina, on_delete=models.CASCADE, related_name='medicoes')
    data_hora = models.DateTimeField(auto_now_add=True)
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    cloro = models.DecimalField(max_digits=4, decimal_places=2)
    alcalinidade = models.DecimalField(max_digits=4, decimal_places=2)
    # Adicione outros campos conforme necessário

    def __str__(self):
        return f"Medição {self.id} para {self.piscina.nome} em {self.data_hora.strftime('%Y-%m-%d %H:%M:%S')}"
