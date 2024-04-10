from django.shortcuts import render, redirect, reverse
from django.http import HttpRequest, HttpResponse
from django_cleanup import cleanup
from django.contrib.auth.decorators import login_required
from .models import Book
from Author.models import Author
from Author.forms import AuthorForm
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, "home.html")

def get_books(request):
    books = Book.objects.all()
    return render(request, "AllBooks.html", context={"books":books})

def bookShow(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'ShowBook.html', context={"book":book})

@login_required
def createBook(request):
    book = Book()
    if request.method == 'POST':
        book.name = request.POST.get('name')
        book.price = request.POST.get('price')
        book.noOfPages = request.POST.get('noOfPages')
        author_name = request.POST.get('author_name')

        try:
            book.author = Author.objects.get(name=author_name)
        except Author.DoesNotExist:
            author_exists = False  
        else:
            author_exists = True  

        # Retrieve and save image file from request.FILES (unchanged)
        if 'image' in request.FILES:
            book.image = request.FILES['image']

        if author_exists:
            book.save()
            return redirect('get books')  
        else:
            messages.error(request, "This author doesn't exist, please enter a valid author name")

    # If request method is GET, render the createBook.html template
    return render(request, 'createBook.html', {'book': book})


def deleteBook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    url = reverse("get books")
    return redirect(url)

def updateBook(request, id):
    book = Book.objects.get(id=id)
    
    if request.method == 'POST':
        book.name = request.POST.get('name', book.name)
        book.price = request.POST.get('price', book.price)
        book.author = request.POST.get('author', book.author)
        book.noOfPages = request.POST.get('noOfPages', book.noOfPages)
        
        # Retrieve and save image file from request.FILES
        if 'image' in request.FILES:
            book.image = request.FILES['image']
        
        book.save()
        
        return redirect("get books")
    
    return render(request, 'createBook.html', context={"book": book})

def addBookAuthor(request, id):
    form = AuthorForm()
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = Author.createAuthor(request.POST['name'], request.POST['bdate'], request.FILES['photo'])
            author.save()  

            book.author = author
            book.save()  

            url = reverse("get authors")
            return redirect(url)
        
    return render(request, 'forms/addAuthor.html', context={"form": form})
