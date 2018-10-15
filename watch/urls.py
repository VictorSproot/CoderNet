from django.urls import path
from .views import *


urlpatterns = [
    path('video/<slug>', category_detail, name='lang_detail_url'),
    path('video/<cat_name>/<slug>', VideoDetail.as_view(), name='video_detail_url'),
]
