from django.db import models

# Son las escuelas a las que los estudiantes pueden ir
class EscuelasMov(models.Model):
    nombre = models.CharField(max_length=150)
    pagina_web = models.CharField(max_length=201)
    pais = models.CharField(max_length=100, editable=True)
    tipo = models.CharField(max_length=100, editable=True)

    def __str__(self):
        return self.nombre

# Son las carreras que cuenta el plan de estudios
class Carreras(models.Model):
    carrera = models.CharField(max_length=150)

    def __str__(self):
        return self.carrera

# Es la relación para ver qué escuela está disponible en qué carrera
class CarrerasInter(models.Model):
    disponible = models.BooleanField(default=False)
    carreras = models.ForeignKey(Carreras, on_delete=models.CASCADE, related_name='carreras_inter')
    escuelas_mov = models.ForeignKey(EscuelasMov, on_delete=models.CASCADE, related_name='carreras_inter')