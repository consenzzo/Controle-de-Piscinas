from django.contrib import admin
from .models import Medicao

@admin.register(Medicao)
class MedicaoAdmin(admin.ModelAdmin):
    list_display = ('piscina', 'data_hora', 'ph', 'cloro', 'alcalinidade')
    list_filter = ('piscina', 'data_hora')
    search_fields = ('piscina__nome',)
