from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from BookApp.models import Book
from .models import Author
from .forms import AuthorForm

# Create your views here.

def allAuthors(request):
    authors = Author.objects.all()
    return render(request, "author/index.html", context={"authors":authors})

def addAuthor(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = Author.createAuthor(request.POST['name'], request.POST['bdate'], request.FILES['photo'])
            url = reverse("get authors")
            return redirect(url)
        print(form.errors)
    return render(request, 'forms/addAuthor.html', context={"form": AuthorForm})

def showAuthor(request, id):
    author = Author.objects.get(id=id)
    if author is not None:
        return render(request, 'author/showAuthor.html', context={"author": author})

def editAuthor(request, id):
    author = Author.objects.get(id=id)
    if author is not None:
        form = AuthorForm(instance=author)
        if request.method == 'POST':
            form = AuthorForm(request.POST, request.FILES, instance=author)
            if form.is_valid():
                form.save()
                return redirect("show author", id=author.id)  
            
        return render(request, 'forms/editAuthor.html', context={"form": form})

def deleteAuthor(request, id):
    author = Author.objects.get(id=id)
    if author is not None:
        author.delete()
        url = reverse("get authors")
        return redirect(url)

def show_author_books(request, id):
    author = get_object_or_404(Author, id=id)
    author_books = list(Book.objects.filter(author=author))
    return render(request, 'author/showBooks.html', context={"author": author, "author_books": author_books})