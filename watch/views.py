from django.shortcuts import render
from .models import *
from .utils import *
from django.views.generic import View
from django.core.paginator import Paginator


# Create your views here.
def video_list(request):
    video = Video.objects.all()
    categories = Category.objects.all()
    context = {
        'video': video,
        'categories': categories
    }
    return render(request, 'booklist/videolist.html', context=context)



class VideoDetail(ObjectDetailMixin, View):
    model = Video
    template = 'booklist/video_detail.html'


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    books = Video.objects.filter(category=category)
    if not category:
        return render(request, '404.html', context={})
        return render(request, 'category_detail.html', context={'category':category})
    # Пагинатор начало
    page_number1 = request.GET.get('page', default=1)
    page1 = paginator1.get_page(page_number1)
    is_paginated1 = page1.has_other_pages()

    if page1.has_previous():
        prev_url1 = '?page={}'.format(page1.previous_page_number())
    else:
        prev_url1 = ''

    if page1.has_next():
        next_url1 = '?page={}'.format(page1.next_page_number())
    else:
        next_url1 = ''
    # Пагинатор конец


    context = {
        'category': category,
        'categories': categories,
        'page_object1': page1,
        'is_paginated1': is_paginated1,
        'prev_url1': prev_url1,
        'next_url1': next_url1,
        'page_object2': page2,
        'is_paginated2': is_paginated2,
        'prev_url2': prev_url2,
        'next_url2': next_url2
    }
    return render(request, 'booklist/video_detail.html', context=context)


