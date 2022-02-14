from django.shortcuts import render
from products.models import ProductCategory, Product


# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'products': Product.objects.all(),
        'menu': ProductCategory.objects.all(),
        'page': [1, 2, 3, 'Next'],
        'title': 'GeekShop - Каталог'
    }
    return render(request, 'products/products.html', context)
