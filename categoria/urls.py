from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.categoria_list, name='categorias'),
    path('categorias/new/', views.categoria_create, name='categoria_create'),
    path('categorias/edit/<int:pk>/', views.categoria_update, name='categoria_update'),
    path('categorias/delete/<int:pk>/', views.categoria_delete, name='categoria_delete'),
]