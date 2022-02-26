from django.shortcuts import render

from users.models import User

def index(request):
    context = {
        'title': 'GeekShop - Admin'
    }
    return render(request, 'admins/index.html', context)


def admin_users(request):
    context = {
        'title': 'GeekShop - Admin',
        'users': User.objects.all(),
        'for': [0, 1]
    }
    return render(request, 'admins/admin-users-read.html', context)