from django.urls import path
from . import views

urlpatterns = [
    path("", views.crud, name="pruebas"),
    path("lista_documentos/", views.lista_documentos, name = "lista_documentos"),
    path("mostrar_formulario/", views.mostrar_formulario, name = "mostrar_formulario"),
]
