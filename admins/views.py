from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView


from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


#Read
class UserAdminListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'


#Create
class UserAdminCreateView(CreateView):
    model = User
    template_name ='admins/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admin_staff:admin_users')


#Update
class UserAdminUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    form_class = UserAdminProfileForm


# class UserAdminDeleteView()


#Delete
@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, pk):
    user = User.objects.get(id=pk)
    user.is_active = False
    user.save_delete()
    messages.success(request, 'Пользователь стал неактивным.')
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))


# #index
# def index(request):
#     context = {
#         'title': 'GeekShop - Admin'
#     }
#     return render(request, 'admins/index.html', context)


#Read
# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     context = {
#         'title': 'GeekShop - Admin',
#         'users': User.objects.all(),
#     }
#     return render(request, 'admins/admin-users-read.html', context)


#Create
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Пользователь успешно создан.')
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegistrationForm()
#     context = {
#         'title': 'GeekShop - Admin',
#         'form': form
#     }
#     return render(request, 'admins/admin-users-create.html', context)


#Update
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, pk):
#     selected_user = User.objects.get(id=pk)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Пользователь успешно редактирован.')
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#
#     context = {
#         'title': 'GeekShop - Admin', 'form': form, 'selected_user': selected_user
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)