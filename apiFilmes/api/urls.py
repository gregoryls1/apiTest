from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('filmes/', FilmesList.as_view()),
    re_path(r'^filmes/(?P<pk>[0-9]+)$', FilmesDetalhes.as_view())
]
