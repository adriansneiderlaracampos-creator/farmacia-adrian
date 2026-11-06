# farmacia/admin.py
from django.contrib import admin
from .models import Medicamento

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'laboratorio', 'precio', 'requiere_receta')
    search_fields = ('nombre_producto', 'laboratorio')
    list_filter = ('requiere_receta', 'laboratorio')