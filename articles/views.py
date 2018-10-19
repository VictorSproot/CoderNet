from django.shortcuts import render
from .models import *


# Create your views here.
def articles_list(request):
    articles = Articles.objects.all()
    categories = Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories
    }
    return render(request, 'articles/article_list.html', context=context)


def article_detail(request, slug):
    article = Articles.objects.get(slug__iexact=slug)
    categories = Category.objects.all()
    context = {
        'article': article,
        'categories': categories
    }
    return render(request, 'articles/article_detail.html', context=context)


def category_detail(request, slug):
    category = Category.objects.get(slug__iexact=slug)
    categories = Category.objects.all()
    context = {
        'category': category,
        'categories': categories
    }
    return render(request, 'articles/category_list.html', context=context)
