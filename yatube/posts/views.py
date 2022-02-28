from django.shortcuts import render
from django.http import HttpResponse


def index(request):    
    return HttpResponse('Главная страница')

def group_posts(request, slug):    
    return HttpResponse('Не главная страница')
# Create your views here.
