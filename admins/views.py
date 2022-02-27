from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm

def index(request):
    context = {
        'title': 'GeekShop - Admin'
    }
    return render(request, 'admins/index.html', context)

#Read
def admin_users(request):
    context = {
        'title': 'GeekShop - Admin',
        'users': User.objects.all(),
        'for': [0, 1]
    }
    return render(request, 'admins/admin-users-read.html', context)

#Create
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно создан.')
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegistrationForm()
    context = {
        'title': 'GeekShop - Admin',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)

#Update
def admin_users_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminProfileForm(instance=selected_user)

    context = {
        'title': 'GeekShop - Admin', 'form': form, 'selected_user': selected_user
    }
    return render(request, 'admins/admin-users-update-delete.html', context)