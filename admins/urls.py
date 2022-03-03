from django.urls import path
from admins.views import UserAdminListViews, UserAdminCreateViews, admin_users_update, admin_users_delete#, index

app_name = 'admins'

urlpatterns = [
    #path('', index, name='index'),
    path('users/', UserAdminListViews.as_view(), name='admin_users'),
    path('users-create/', UserAdminCreateViews.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', admin_users_update, name='admin_users_update'),
    path('users-delete/<int:pk>/', admin_users_delete, name='admin_users_delete'),
]