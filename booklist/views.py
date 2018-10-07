from django.shortcuts import render
from .models import *
from .utils import *
from django.views.generic import View


# Create your views here.
def book_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    context = {
        'books': books,
        'categories': categories
    }
    return render(request, 'booklist/booklist.html', context=context)


class CategoryDetail(ObjectDetailMixin, View):
    model = Category
    template = 'booklist/category_detail.html'


class BookDetail(ObjectDetailMixin, View):
    model = Book
    template = 'booklist/book_detail.html'
