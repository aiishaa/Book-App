from django.urls import path
from .views import bookShow, createBook, deleteBook, updateBook, get_books, home, addBookAuthor

urlpatterns = [
    path('books/', get_books, name="get books"),
    path('books/<int:id>', bookShow, name="Book show"),
    path('createBook', createBook, name="create book"),
    path('books/deleteBook/<int:id>', deleteBook, name='delete book'),
    path('books/updateBook/<int:id>', updateBook, name='update book'),
    path('books/addBookAuthor/<int:id>', addBookAuthor, name='add book author'),
]