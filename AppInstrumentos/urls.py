from django.urls import path
from AppInstrumentos.views import *

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("agregar_bajos/", agregar_bajos, name= "agregar_bajos"),
    path("agregar_baterias/", agregar_baterias, name= "agregar_baterias"),
    path("agregar_guitarras/", agregar_guitarras, name= "agregar_guitarras"),
    path("busqueda_db/", busqueda_db, name= "busqueda_db"),
    path("resultado/", resultado_busqueda, name = "resultado_busqueda"),
]