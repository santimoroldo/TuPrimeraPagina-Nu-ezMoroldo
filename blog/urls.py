from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('autor-formulario/', views.autor_formulario, name="AutorFormulario"),
    path('seccion-formulario/', views.seccion_formulario, name="SeccionFormulario"),
    path('post-formulario/', views.post_formulario, name="PostFormulario"),
    path('busqueda-autor/', views.busqueda_autor, name="BusquedaAutor"),
    path('resultados-busqueda/', views.resultados_busqueda, name="ResultadosBusqueda"),
]
