from django.shortcuts import render
from .models import Autor, Seccion, Post
from .forms import AutorFormulario, SeccionFormulario, PostFormulario
from django.http import HttpResponse

def inicio(request):
    return render(request, "blog/padre.html")

def autor_formulario(request):
    if request.method == "POST":
        mi_formulario = AutorFormulario(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            nuevo_autor = Autor(nombre=info['nombre'], apellido=info['apellido'], email=info['email'])
            nuevo_autor.save()
            
            return render(request, "blog/padre.html", {"mensaje": "¡Autor creado con éxito!"})
    else:
        mi_formulario = AutorFormulario()
    return render(request, "blog/autor_formulario.html", {"mi_formulario": mi_formulario})

def seccion_formulario(request):
    if request.method == "POST":
        mi_formulario = SeccionFormulario(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            nueva_seccion = Seccion(nombre=info['nombre'])
            nueva_seccion.save()
            return render(request, "blog/padre.html", {"mensaje": "¡Sección creada con éxito!"})
    else:
        mi_formulario = SeccionFormulario()
    
    
    return render(request, "blog/seccion_formulario.html", {"mi_formulario": mi_formulario})

def post_formulario(request):
    if request.method == "POST":
        mi_formulario = PostFormulario(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            
            # Ajustamos los nombres para que coincidan con tu MODELS.PY
            nuevo_post = Post(
                titulo=info['titulo'], 
                contenido=info['cuerpo'], # Guardamos lo que viene de 'cuerpo' en 'contenido'
                fecha="2026-03-14"        # Le pasamos una fecha manual para que no falle (podes usar timezone.now() despues)
            )
            nuevo_post.save()
            return render(request, "blog/padre.html", {"mensaje": "¡Post creado con éxito!"})
    else:
        mi_formulario = PostFormulario()
    
    return render(request, "blog/post_formulario.html", {"mi_formulario": mi_formulario})


def busqueda_autor(request):
    return render(request, "blog/busqueda_autor.html")

def resultados_busqueda(request):
    nombre_buscado = request.GET.get("nombre")
    
def resultados_busqueda(request):
    nombre_buscado = request.GET.get("nombre")
    
    if nombre_buscado:
        autores = Autor.objects.filter(nombre__icontains=nombre_buscado)
        return render(request, "blog/resultados_busqueda.html", {"autores": autores, "query": nombre_buscado})
    else:
        return render(request, "blog/busqueda_autor.html", {"error": "No ingresaste ningún nombre"})