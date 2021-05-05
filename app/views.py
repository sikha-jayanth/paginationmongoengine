from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView
from .serializers import BookSerializer
from rest_framework import filters
from .models import Books1
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.
class MyOffsetPagination(LimitOffsetPagination): #pagination class
    default_limit = 2
    max_limit = 5

    
class BookListView(ListAPIView):
    serializer_class=BookSerializer
    my_filter_fields = ('language',)
    pagination_class = MyOffsetPagination

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {} 

        for field in  self.my_filter_fields: # iterate over the filter fields
            field_value = self.request.query_params.get(field) # get the value of a field from request query parameter
            if field_value: 
                filtering_kwargs[field] = field_value
        return filtering_kwargs 

    def get_queryset(self):
        queryset = Books1.objects.all() 
        filtering_kwargs = self.get_kwargs_for_filtering() # get the fields with values for filtering 
        if filtering_kwargs:
            queryset = Books1.objects.filter(**filtering_kwargs) # filter the queryset based on 'filtering_kwargs'
        return queryset

class BookCreateView(CreateAPIView):
    serializer_class=BookSerializer
    
