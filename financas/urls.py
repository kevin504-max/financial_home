from django.urls import path
from . import views

urlpatterns = [
    path('gastos/', views.gastos_list, name='gastos'),
    path('gastos/new/', views.gastos_create, name='gastos_create'),
    path('gastos/edit/<int:pk>/', views.gastos_update, name='gastos_update'),
    path('gastos/delete/<int:pk>/', views.gastos_delete, name='gastos_delete'),

    path('gastos/exportar/', views.exportar_csv, name='exportar_csv'),
]
