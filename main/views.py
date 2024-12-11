from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return HttpResponse('About page')

def catalog(request):
    return render(request, 'main/catalog.html')

def profile(request):
    return HttpResponse('Profile')

def cart(request):
    return HttpResponse('Cart')

def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')