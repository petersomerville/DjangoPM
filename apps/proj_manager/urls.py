from django.urls import path
from . import views

app_name = 'proj_manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit_proj/<int:proj_id>', views.edit_proj, name = 'edit_proj'),

]