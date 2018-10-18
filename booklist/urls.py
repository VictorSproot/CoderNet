from django.urls import path
from .views import *


urlpatterns = [
    path('', book_list, name='book_list_url'),
    path('book/<slug>', category_detail, name='category_detail_url'),
    path('book/<cat_name>/<slug>', BookDetail.as_view(), name='book_detail_url'),
]


