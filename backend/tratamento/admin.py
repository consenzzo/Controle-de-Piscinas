from django.contrib import admin
from .models import ParametrosTratamento, RecomendacaoTratamento

@admin.register(ParametrosTratamento)
class ParametrosTratamentoAdmin(admin.ModelAdmin):
    list_display = ('parametro', 'valor_minimo', 'valor_maximo')
    search_fields = ('parametro',)

@admin.register(RecomendacaoTratamento)
class RecomendacaoTratamentoAdmin(admin.ModelAdmin):
    list_display = ('medicao', 'recomendacoes')
    search_fields = ('medicao__piscina__nome',)
