from django.urls import path
from .views import inicio, obtener_estados, obtener_municipios

urlpatterns = [
    path('', inicio, name='inicio'),
    path('obtener_estados/', obtener_estados, name='obtener_estados'),
    path('obtener_municipios/', obtener_municipios, name='obtener_municipios'),
]