from django.urls import path
from app.views import *

urlpatterns = [
    path('booklist',BookListView.as_view(),name='booklist'),
    path('create',BookCreateView.as_view(),name='create'),
]