from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from doge.models import Book
from datetime import date
from doge.models import Doge
from doge.models import Kit
from doge.models import Author
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound


def bookList(request):
    return render(request, 'doge/books.html', {'data': {
        'current_date': date.today(),
        'books': Book.objects.all(),
        'dogs': Doge.objects.all(),
        'cats': Kit.objects.all(),
        'author': Author.objects.all()
    }})


def GetBook(request, id):
    return render(request, 'doge/book.html', {'data': {
        'current_date': date.today(),
        'book': Book.objects.filter(id=id)[0],
        'author': Author.objects.filter()
    }})



def GetDog(request, id):
    return render(request, 'doge/dog.html', {'data': {
        'dog': Doge.objects.filter(id=id)[0]
    }})

def delete_Book(request, id):
    book = get_object_or_404(Book, id=id)
    try:
        book.delete()
        return HttpResponseRedirect("/")
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>file not found</h2>")

def delete_Author(request, idauthor):
    author = get_object_or_404(Author, idauthor=idauthor)
    try:
        author.delete()
        return HttpResponseRedirect("/")
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>file not found</h2>")

def create(request):
     if request.method == "POST":
        dl = Author(authorname = request.POST.get("Authorname") ,authorbio=request.POST.get("Authorbio"))

        dl.save()
     return HttpResponseRedirect("/")


def create_book(request):
    if request.method == "POST":
        book = Book(name=request.POST.get("name"), dicription=request.POST.get("dicription"), bookauthor = Author.objects.get(idauthor=request.POST.get("bookauthorr")))
        book.save()
    return HttpResponseRedirect("/")
def edit(request, id):
    try:
        book = Book.objects.get(id=id)
        if request.method == "POST":
            book.name = request.POST.get("name")
            book.dicription = request.POST.get("discription")
            book.bookauthor.idAuthor = Author.objects.get(idauthor=request.POST.get("bookauthorr"))
            book.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "doge/edit.html", {"book": book})
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>file not found</h2>")

def edit_Author(request, idAuthor):
    try:
        author = Author.objects.get(idauthor=idAuthor)
        if request.method == "POST":
            author.authorname = request.POST.get("authorname")
            author.authorbio = request.POST.get("authorbio")
            author.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "doge/edit_author.html", {"author": author})
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>file not found</h2>")



def GetKit(request, id):
    return render(request, 'doge/kit.html', {'data': {

        'cat': Kit.objects.filter(id=id)[0]
    }})


def index(request):
    return render(request, 'doge/index.html')


def about(request):
    return render(request, 'doge/about.html')


def Siba(request):
    return render(request, 'doge/Siba.html')


def bull_terrier(request):
    return render(request, 'doge/bull_terrier.html')


def jack(request):
    return render(request, 'doge/jack.html')
