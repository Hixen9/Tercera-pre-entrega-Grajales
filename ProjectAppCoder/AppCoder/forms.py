from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()

class ProfesoresFormulario(forms.Form):

    nombre = forms.CharField( max_length=50)
    apellido = forms.CharField( max_length=50)
    email = forms.EmailField( max_length=254) 
    Profesion = forms.CharField( max_length=50)

class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField( max_length=50)
    apellido = forms.CharField( max_length=50)
    email = forms.EmailField( max_length=254) 

class EntregablesFormulario(forms.Form):
    nombre = forms.CharField( max_length=50)
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()