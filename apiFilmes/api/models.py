from django.db import models

# Create your models here.

class Filmes(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    genero = models.CharField(max_length=30, null=False)
    ano = models.FloatField(null=False)
    sinopse = models.CharField(max_length=600, null=False)

    def __str__(self):
        return self.titulo
