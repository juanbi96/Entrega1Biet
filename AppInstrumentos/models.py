from django.db import models

# Create your models here.
class Guitarras(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    año_fabricacion = models.IntegerField()
    cuerdas = models.IntegerField()

    def __str__(self):
        return self.marca +" "+ self.modelo
        
class Bajos(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    año_fabricacion = models.IntegerField()
    cuerdas = models.IntegerField()

    def __str__(self):
        return self.marca +" "+ self.modelo

class Baterias(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    año_fabricacion = models.IntegerField()
    
    def __str__(self):
        return self.marca +" "+ self.modelo