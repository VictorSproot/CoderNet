from django.urls import path
from .views import *


urlpatterns = [
    path('', book_list, name='book_list_url'),
    path('<slug>', CategoryDetail.as_view(), name='category_detail_url'),
    path('<cat_name>/<slug>', BookDetail.as_view(), name='book_detail_url'),
]
