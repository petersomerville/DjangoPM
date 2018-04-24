from django.urls import path
from . import views

app_name = 'proj_manager'

urlpatterns = [
    path('', views.index, name='index'),

    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('register_post', views.register_post, name = 'register_post'),
    path('login_post', views.login_post, name = 'login_post'),

    path('create_proj', views.create_proj, name = 'create_proj'),
    path('delete_proj/<int:proj_id>', views.delete_proj, name = 'delete_proj'),
    path('edit_proj/<int:proj_id>', views.edit_proj, name = 'edit_proj'),
    path('update_proj/<int:proj_id>', views.update_proj, name = 'update_proj'),

]

