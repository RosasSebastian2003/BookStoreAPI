from django.contrib import admin
from .models import Book, Author, Member, Borrowing

# Register your models here.
# Admin Classes
class BookAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'isbn', 'authorId__name']
    list_filter = ['authorId__name']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class MemberAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'email']

class BorrowingAdmin(admin.ModelAdmin):
    list_display = ['bookId', 'memberId', 'borrowDate', 'returnDate']
    search_fields = ['bookId__title', 'memberId__name']
    list_filter = ['borrowDate', 'returnDate']

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Borrowing, BorrowingAdmin)