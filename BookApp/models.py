from django.db import models
from Author.models import Author
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(default=0)
    noOfPages = models.IntegerField(default=100)
    image = models.ImageField(upload_to='books/images/', null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True) # create
    updated_at = models.DateTimeField(auto_now=True)  # update

    def __str__(self):
        return f"{self.name}" 
    
    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @property
    def show_author(self):
        return reverse('show author', args=[self.author.id])
    
    @property
    def edit_author(self):
        return reverse('edit author', args=[self.author.id])
    