from django.shortcuts import render, redirect


def main_page(request):
    return render(request, 'booklist/home.html')  