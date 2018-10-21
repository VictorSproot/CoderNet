from django.shortcuts import render, redirect
from video.models import Course
from articles.models import Articles
from booklist.models import Book


def main_page(request):
    return render(request, 'booklist/home.html')


def search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        books = Book.objects.filter(title__icontains=search_query)
        courses = Course.objects.filter(title__icontains=search_query)
        articles = Articles.objects.filter(title__icontains=search_query)
        context = {
            'books': books,
            'courses': courses,
            'articles': articles
        }
        return render(request, 'booklist/search.html', context=context)
    else:
        return render(request, 'booklist/404.html')
