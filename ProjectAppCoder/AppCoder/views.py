from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def inicio(request):

    if request.GET["camada"]:

            camada = request.GET["camada"]
            cursos = Curso.objects.filter(camada=camada)
            return render(request, "resultadoCamada.html", {"cursos": cursos, "camada": camada})
    else:
        return HttpResponse(f'No enviaste info')

def profesores(request):
    if request.method == 'POST':
        miFormulario = ProfesoresFormulario(request.POST)

        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'],email=data['email'], Profesion=data['Profesion'])
            profesor.save()
            print(request.POST)
            return render(request, "inicio.html")
        else:
            return render(request, "inicio.html",{"mensaje": "Formulario Invalido"})
    else:
        miFormulario =ProfesoresFormulario()
        return render(request, "profesores.html", {"miFormulario": miFormulario })

def estudiantes(request):
    if request.method == 'POST':
        miFormulario = EstudiantesFormulario(request.POST)

        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=data['nombre'], apellido=data['apellido'],email=data['email'])
            estudiante.save()
            return render(request, "inicio.html")
        else:
            return render(request, "inicio.html",{"mensaje": "Formulario Invalido"})
    else:
        miFormulario =EstudiantesFormulario()
        return render(request, "estudiantes.html", {"miFormulario": miFormulario })

def entregables(request):
    if request.method == 'POST':
        miFormulario = EntregablesFormulario(request.POST)

        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            entregable = Entregable(nombre=data['nombre'], fecha_entrega=data['fecha_entrega'], entregado=data['entregado'])
            entregable.save()
            return render(request, "inicio.html")
        else:
            return render(request, "inicio.html",{"mensaje": "Formulario Invalido"})
    else:
        miFormulario =EntregablesFormulario()
        return render(request, "entregables.html", {"miFormulario": miFormulario })
def cursoFormulario(request):

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)

        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            curso = Curso(nombre=data['curso'], camada=data['camada'])
            curso.save()
            return render(request, "inicio.html",{"mensaje": "Formulario VALIDO!"})
        else:
            return render(request, "inicio.html",{"mensaje": "Formulario Invalido"})
    else:
        miFormulario = CursoFormulario()
        return render(request, "cursoFormulario.html", {"miFormulario": miFormulario })
    
def buscarCamada(request):

    return render(request, "inicio.html")