from django.http import JsonResponse
from django.shortcuts import render
from .models import Estado, Municipio
import json
# Create your views here.
def inicio(request):
    return render(request, 'ubicaciones/inicio.html')

def obtener_estados(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        estados = list(Estado.objects.values('id', 'nombre'))
        return JsonResponse({'estados': estados})
    return JsonResponse({'error': 'Solicitud inválida'}, status=400)

def obtener_municipios(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == 'POST':
        data = json.loads(request.body)
        estado_id = data.get('estado_id')
        if estado_id:
            municipios = list(Municipio.objects.filter(estado_id=estado_id).values('id', 'nombre'))
            return JsonResponse({'municipios': municipios})
        return JsonResponse({'error': 'No se seleccionó un estado'}, status=400)
    return JsonResponse({'error': 'Solicitud inválida'}, status=400)