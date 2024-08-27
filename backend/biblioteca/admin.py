from django.contrib import admin
from .models import ProblemaComum

@admin.register(ProblemaComum)
class ProblemaComumAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo', 'descricao')
