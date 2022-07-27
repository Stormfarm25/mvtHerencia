from django.urls import path

from AppFamilia.views import Inicio, Padres, Hermanos , Abuelos

# Codigo de Vitor Lira , PrimerMVT - Coder.

urlpatterns = [
    path('', Inicio),
    path('padres/',Padres),
    path('hermanos/', Hermanos),
    path('abuelos/', Abuelos),
]
