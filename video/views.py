from django.shortcuts import render
from .models import *


# Create your views here.
def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'video/category_list.html', context=context)


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'category': category
    }
    return render(request, 'video/category_detail.html', context=context)


def course_detail(request, **kwargs):
    categories = Category.objects.all()
    course = Course.objects.get(slug=kwargs['slug'])
    context = {
        'categories': categories,
        'course': course
    }
    return render(request, 'video/course_detail.html', context=context)
