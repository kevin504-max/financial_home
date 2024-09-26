from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuario_list, name='usuarios'),
    path('usuarios/new/', views.usuario_create, name='usuario_create'),
    path('usuarios/edit/<int:pk>/', views.usuario_update, name='usuario_update'),
    path('usuarios/delete/<int:pk>/', views.usuario_delete, name='usuario_delete'),

    path('usuarios/exportar/', views.exportar_csv, name='exportar_usuarios_csv'),
]
