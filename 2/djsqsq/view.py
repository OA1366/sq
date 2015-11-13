#!/usr/bin/python
# -*- encoding: utf-8 -*-
#from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from books.models import Book, Author


def hello(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    return render_to_response('home.html', locals())


def search(request):
    error = False  
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            error = True
        else:
            books = Book.objects.filter(AuthorID__Name=query)
            return render_to_response('search_from.html',locals())
    return render_to_response('search_from.html',locals())

def find(request):
    ID = request.GET['id']
    book = Book.objects.get(id=ID)
    author = book.AuthorID.Name
    return render_to_response('findauthor.html',locals())

def show(request):
    ID = request.GET['id']
    operate = request.GET['sq']
    book = Book.objects.get(id=ID)
    if operate == "Delete":
         book.delete()
    else:
        return render_to_response('update.html',locals())
    books = Book.objects.all()
    authors = Author.objects.all()
    return render_to_response('home.html',locals())
    
def update(request):
    books = Book.objects.all()
    if request.POST:
        name = request.POST['name']
        ID = request.POST['id']
        try:
            author = Author.objects.get(Name=name)
        except:
            return render_to_response('addAuthor.html',locals())
        else:
            book = Book.objects.get(id=ID)
            book.AuthorID = author 
            book.Publisher = request.POST['publisher']
            book.Title = request.POST['title']
            book.PublishDate = request.POST['publishdate']
            book.Price = request.POST['price']
            book.save()
            authors = Author.objects.all()
    return render_to_response('home.html',locals())

def addAuthor(request):
    ID = request.POST['id']
    name = request.POST['name']
    age = request.POST['age']
    country = request.POST['country']
    author = Author(Name=name,Age=age,Country=country)
    author.save()
    book = Book.objects.get(id=ID)
    return render_to_response('update.html',locals())

def delauthor(request):
    ID = request.GET['id']
    author = Author.objects.get(id=ID)
    author.delete()
    books = Book.objects.all()
    authors = Author.objects.all()
    return render_to_response('home.html',locals())

def addbook(request):
    if request.POST:
        name = request.POST['name']
        try:
            author = Author.objects.get(Name=name)
        except:
            return render_to_response('addau.html',)

        else:
            book = Book()
            book.AuthorID = author 
            book.Publisher = request.POST['publisher']
            book.Title = request.POST['title']
            book.PublishDate = request.POST['publishdate']
            book.Price = request.POST['price']
            book.save()
            books = Book.objects.all()
            authors = Author.objects.all()
            return render_to_response('home.html',locals())
    else:
        return render_to_response('addbook.html',)
def addau(request):
    name = request.POST['name']
    age = request.POST['age']
    country = request.POST['country']
    author = Author(Name=name,Age=age,Country=country)
    author.save()
    return render_to_response('addbook.html',)
    
    
    
    
    
