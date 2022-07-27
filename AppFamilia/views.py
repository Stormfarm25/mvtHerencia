from re import A
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
from AppFamilia.models import Familia
# Create your views here.
# Codigo de Vitor Lira , PrimerMVT - Coder.
def Inicio(request):
    plantilla = loader.get_template('FamiliaInicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def Padres(self):
    madre = Familia(nombre = "Sara", apellido= "Goldstein", edad = 36, fechaNacimiento = "1986-07-27", ocupacion = "Enfermera")
    madre.save()
    plantilla = loader.get_template('padres.html')
    documentoTexto = {'nombre': madre.nombre,'apellido': madre.apellido,'edad':madre.edad,'fn':madre.fechaNacimiento,'ocupacion':madre.ocupacion }
    documento = plantilla.render(documentoTexto)
    return HttpResponse(documento)

def Hermanos(self):
    hermana = Familia(nombre = "Martina", apellido= "Goldstein", edad = 7, fechaNacimiento = "2015-01-25", ocupacion = "Estudiante")
    hermana.save()
    plantilla = loader.get_template('hermanos.html')
    documentoTexto = {'nombre': hermana.nombre, 'apellido': hermana.apellido,'edad':hermana.edad,'fn':hermana.fechaNacimiento,'ocupacion':hermana.ocupacion}
    documento = plantilla.render(documentoTexto)
    return HttpResponse(documento)

def Abuelos(self):
    abuela = Familia(nombre = "Maria", apellido= "Goldstein", edad = 59, fechaNacimiento = "1963-02-04", ocupacion = "Jubilada")
    abuela.save()
    plantilla = loader.get_template('abuelos.html')
    documentoTexto = {'nombre': abuela.nombre,'apellido': abuela.apellido,'edad':abuela.edad,'fn':abuela.fechaNacimiento,'ocupacion':abuela.ocupacion}
    documento = plantilla.render(documentoTexto)
    
    return HttpResponse(documento)

