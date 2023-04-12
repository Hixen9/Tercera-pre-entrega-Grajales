from django.contrib import admin
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('',buscarCamada,name = "Inicio"),
    path('estudiantes/',estudiantes, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
    path('entregables/',entregables, name="Entregables"),
    path('cursoFormulario/',cursoFormulario, name="CursoFormulario"),
    path('resultadoCamada/',inicio, name="Buscar")
]