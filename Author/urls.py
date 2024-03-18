from django.urls import path
from .views import addAuthor, allAuthors, editAuthor, showAuthor, deleteAuthor, show_author_books

urlpatterns = [
    path('allAuthors', allAuthors, name="get authors"),
    path('forms/addAuthor', addAuthor, name='add author'),
    path('forms/editAuthor/<int:id>', editAuthor, name='edit author'),
    path('showAuthor/<int:id>', showAuthor, name='show author'),
    path('deleteAuthor/<int:id>', deleteAuthor, name='delete author'),
    path('showAuthorBooks/<int:id>', show_author_books, name='show author books')
]