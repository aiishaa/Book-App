from django.db import models
from django.shortcuts import reverse, redirect

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bdate = models.DateField(null=True)
    photo = models.ImageField(upload_to='authors/images', null=True)

    @classmethod
    def createAuthor(cls, name, bdate, photo):
        try:
            author = cls(name=name, bdate=bdate, photo=photo)
            author.save()
        except Exception as e:
            return False
        else:
            return author
    
    def __str__(self):
        return self.name
    
    @property
    def photo_url(self):
        return f"/media/{self.photo}"
    
    @property
    def getAuthors(self):
        return reverse('get authors')
    
    @property
    def show_author(self):
        return reverse('show author', args=[self.id]) 
    
    @property
    def edit_author(self):
        return reverse('edit author', args=[self.id])
    
    @property
    def delete_author(self):
        return reverse('delete author', args=[self.id])
