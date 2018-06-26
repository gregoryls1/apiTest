from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .serializers import *
from .pagination import *
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


class FilmesList(APIView):
    def get(self, request):
        try:
            lista_filmes = Filmes.objects.all()
            paginacao = PaginacaoFilmes()
            resultado_pagina = paginacao.paginate_queryset(lista_filmes, request)
            serializer = FilmesSerializer(resultado_pagina, many=True)
            return paginacao.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = FilmesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor" },
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FilmesDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            filmes = Filmes.objects.get(pk=pk)
            serializer = FilmesSerializer(filmes)
            return Response(serializer.data)
        except Filmes.DoesNotExist:
            return JsonResponse({'mensagem': "Filme nao existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            filmes = Filmes.objects.get(pk=pk)
            serializer = FilmesSerializer(filmes, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Filmes.DoesNotExist:
            return JsonResponse({'mensagem': "Filme nao existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            filmes = Filmes.objects.get(pk=pk)
            filmes.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Filmes.DoesNotExist:
            return JsonResponse({'mensagem': "Filme nao existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
