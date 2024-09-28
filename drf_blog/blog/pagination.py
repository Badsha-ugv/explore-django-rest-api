from rest_framework.pagination import PageNumberPagination

class ListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'size'
    last_page_strings = ('last',)
    # max_page_size = 3
    
    