from django.db import models
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    authorId = models.AutoField(primary_key=True, verbose_name='Author ID')
    name = models.CharField(max_length=100)
    biography = models.TextField()

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    
    def __str__(self): # String representation of the object, will display the name of the author instead of Author object
        return self.name

class Book(models.Model):
    bookId = models.AutoField(primary_key=True) # Primary Key
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    publicationYear = models.IntegerField()
    authorId = models.ForeignKey(Author, on_delete=models.CASCADE, null = True)

    boobkCover = models.ImageField(upload_to='bookCovers/', null=True) # Image Field

    def __str__(self): # String representation of the object, will display the book's tittle instead of Book object
        return self.title

class Member(models.Model):
    memberId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self): # String representation of the object, will display the member's name instead of Member object
        return self.name

class Borrowing(models.Model):
    borrowingId = models.AutoField(primary_key=True)
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE)
    memberId = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrowDate = models.DateField(default=timezone.now)
    returnDate = models.DateField(default=timezone.now)


