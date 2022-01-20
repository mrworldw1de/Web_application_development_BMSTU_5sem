from django.shortcuts import render
from django.http import HttpResponse
from doge.models import Book
from datetime import date
from doge.models import Doge
from doge.models import Kit
def bookList(request):
    return render(request, 'doge/books.html', {'data' : {
        'current_date': date.today(),
        'books': Book.objects.all(),
        'dogs': Doge.objects.all(),
        'cats': Kit.objects.all()
    }})
def GetBook(request, id):
    return render(request, 'doge/book.html', {'data' : {
        'current_date': date.today(),
        'book': Book.objects.filter(id=id)[0]
    }})
def GetDog(request, id):
    return render(request, 'doge/dog.html', {'data' : {
        'dog': Doge.objects.filter(id=id)[0]
    }})
def GetKit(request, id):
    return render(request, 'doge/kit.html', {'data' : {

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
    