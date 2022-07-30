from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=30,unique=True)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fechaNacimiento = models.DateField()
    ocupacion = models.CharField(max_length=30)


# Create your models here.
class Tareas(models.Model):
    nombre = models.CharField(max_length=30,unique=True) 
    # responsables = models.CharField(max_length=30)
    creado = models.DateTimeField()


# Create your models here.
class Herramientas(models.Model):
    nombre = models.CharField(max_length=30,unique=True)
    tipo_de_tarea = models.CharField(max_length=30,unique=True)
    responsable_de_uso = models.CharField(max_length=30)
    is_used =  models.BooleanField()