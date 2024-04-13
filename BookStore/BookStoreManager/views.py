from django.shortcuts import render

from rest_framework import viewsets
from .models import Book, Author, Member, Borrowing
from .serializers import BookSerializer, AuthorSerializer, MemberSerializer, BorrowingSerializer

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet): 
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    