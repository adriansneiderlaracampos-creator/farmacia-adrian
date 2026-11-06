# farmacia/views.py
from django.shortcuts import render
from .models import Medicamento

def lista_medicamentos(request):
    # Consulta al ORM
    medicamentos = Medicamento.objects.all()
    
    context = {
        'medicamentos': medicamentos,
        'total_medicamentos': medicamentos.count()
    }
    return render(request, 'farmacia/lista_medicamentos.html', context)