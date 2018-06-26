from rest_framework import serializers
from .models import *


class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = ["id", "titulo", "genero", "ano", "sinopse"]