from django.shortcuts import render, redirect, reverse
from django.http import HttpRequest, HttpResponse
from django_cleanup import cleanup
from django.contrib.auth.decorators import login_required
from .models import Book
from Author.models import Author


# Create your views here.

books = [
    {"id": 1, "name":"Cendrilla", "price": "2000$", "image": "book1.jfif", "author": "Charles Perrault", "noOfPages": 440},
    {"id": 2, "name":"Poor Folk", "price": "1000$", "image": "book2.jfif", "author": "Fyodor Dostoevsky", "noOfPages": 550},
    {"id": 3, "name":"Les miserable", "price": "500$", "image": "book3.jfif", "author":"Victor Hugo", "noOfPages": 660},
    {"id": 4, "name":"Origin", "price": "1500$", "image": "book4.jfif", "author":"Dan Brown", "noOfPages": 770}
]

# @login_required(login_url='/users/login')
def bookInfo(request, id):
    filtered_book = filter(lambda book: book['id'] == id, books)
    filtered_book = list(filtered_book)
    if filtered_book:
        return render(request, "bookInfo.html", context={"book":filtered_book[0]})
    return HttpResponse("Book bot found")

def home(request):
    return render(request, "home.html")

# def allbooks(request):
#     return render(request, "allbooks.html", context={"books":books})

def get_books(request):
    books = Book.objects.all()
    return render(request, "index.html", context={"books":books})

def bookShow(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'show.html', context={"book":book})

@login_required(login_url='/users/login')
def createBook(request):
    if request.method == 'POST':
        book = Book()
        book.name = request.POST.get('name', '')
        book.price = request.POST.get('price', 0)
        book.noOfPages = request.POST.get('noOfPages', 0)
        author_name = request.POST.get('author_name')

        try:
            book.author = Author.objects.get(name=author_name)
        except Author.DoesNotExist:
            book.author = Author.objects.create(name=author_name)

        # Retrieve and save image file from request.FILES
        if 'image' in request.FILES:
            book.image = request.FILES['image']
        
        book.save()

        return redirect('get books')

    # If request method is GET, render the createBook.html template
    return render(request, 'createBook.html')

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
