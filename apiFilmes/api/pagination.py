from  rest_framework import pagination


class PaginacaoFilmes(pagination.PageNumberPagination):
    page_size = 2
    page_query_param = 'pagina'
    page_size_query_param = 'reg_pagina'
    max_page_size = 5