from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
             'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', 'photo': 'vendor/img/products/Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00',
             'text':' Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.', 'photo': 'vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390,
             'text':'Материал с плюшевой текстурой. Удобный и мягкий.', 'photo': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340,
            'text':'Плотная ткань. Легкий материал.', 'photo': 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590,
             'text':'Гладкий кожаный верх. Натуральный материал.', 'photo': 'vendor/img/products/Black-Dr-Martens-shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890,
             'text':'Легкая эластичная ткань сирсакер Фактурная ткань.', 'photo': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'}
        ],
        'menu': ['Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'],
        'page': [1, 2, 3, 'Next'],
        'title': 'GeekShop - Каталог'
    }
    return render(request, 'products/products.html', context)
