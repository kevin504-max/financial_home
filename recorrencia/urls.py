from django.urls import path
from . import views

urlpatterns = [
    path('recorrencias/', views.recorrencia_list, name='recorrencias'),
    path('recorrencias/new/', views.recorrencia_create, name='recorrencia_create'),
    path('recorrencias/edit/<int:pk>/', views.recorrencia_update, name='recorrencia_update'),
    path('recorrencias/delete/<int:pk>/', views.recorrencia_delete, name='recorrencia_delete'),

    path('recorrencias/exportar/', views.exportar_csv, name='exportar_recorrencias_csv'),
]