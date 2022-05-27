from django.shortcuts import render
from products.models import Category

def home(request):
    return render(request, 'base/home.html')
