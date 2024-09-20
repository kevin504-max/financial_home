from django.urls import path
from financas import views

urlpatterns = [
    path('', views.home, name='home'),
]
