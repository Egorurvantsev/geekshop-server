from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


#Read
class UserAdminListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserAdminListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'GeekShop - Admin'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminListView, self).dispatch(request, *args, **kwargs)

#Create
class UserAdminCreateView(CreateView):
    model = User
    template_name ='admins/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admin_staff:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserAdminCreateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'GeekShop - Admin'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminCreateView, self).dispatch(request, *args, **kwargs)


#Update
class UserAdminUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    form_class = UserAdminProfileForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserAdminUpdateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'GeekShop - Admin'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminUpdateView, self).dispatch(request, *args, **kwargs)


#Delete
class UserAdminDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.save_delete()
        return HttpResponseRedirect(self.success_url)



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


#Delete
@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, pk):
    user = User.objects.get(id=pk)
    user.is_active = False
    user.save_delete()
    messages.success(request, 'Пользователь стал неактивным.')
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))