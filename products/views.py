from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)

def products(request, category_id=None):
    context = {
        'page': [1, 2, 3, 'Next'],
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all()
    }
    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()
    context['products'] = products
    return render(request, 'products/products.html', context)