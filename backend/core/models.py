from django.db import models
from accounts.models import User

class Piscina(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='piscinas')
    comprimento = models.DecimalField(max_digits=5, decimal_places=2)
    largura = models.DecimalField(max_digits=5, decimal_places=2)
    profundidade = models.DecimalField(max_digits=5, decimal_places=2)
    forma = models.CharField(max_length=50, choices=[('retangular', 'Retangular'), ('circular', 'Circular')])
    volume = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def calcular_volume(self):
        if self.forma == 'retangular':
            return self.comprimento * self.largura * self.profundidade
        # Adicione lógica para outras formas
        return 0

    def save(self, *args, **kwargs):
        self.volume = self.calcular_volume()
        super(Piscina, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} ({self.usuario.email})"
