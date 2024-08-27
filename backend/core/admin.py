from django.contrib import admin
from .models import Piscina

@admin.register(Piscina)
class PiscinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario', 'volume', 'forma')
    search_fields = ('nome', 'usuario__email')
    list_filter = ('forma',)
