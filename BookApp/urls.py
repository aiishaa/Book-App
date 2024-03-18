from django.urls import path
from .views import bookInfo, bookShow, createBook, deleteBook, updateBook, get_books, home

urlpatterns = [
    # path('allbooks/', allbooks, name="All books"),
    # path('<int:id>', bookInfo, name="Book info"),
    path('books/', get_books, name="get books"),
    path('books/<int:id>', bookShow, name="Book show"),
    path('createBook', createBook, name="create book"),
    path('books/<int:id>/deleteBook', deleteBook, name='delete book'),
    path('books/<int:id>/updateBook', updateBook, name='update book'),
]