from django.shortcuts import render, redirect
from django.views.generic import View


def main_page(request):
    return render(request, 'booklist/home.html')  