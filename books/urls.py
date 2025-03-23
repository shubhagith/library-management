from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView, book_list

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
    path('books/list/', book_list, name='book-list-html'), 
]
