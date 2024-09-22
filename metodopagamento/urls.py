from django.urls import path
from . import views

urlpatterns = [
    path('metodos_pagamento/', views.metodo_pagamento_list, name='metodos_pagamento'),
    path('metodos_pagamento/new/', views.metodo_pagamento_create, name='metodo_pagamento_create'),
    path('metodos_pagamento/edit/<int:pk>/', views.metodo_pagamento_update, name='metodo_pagamento_update'),
    path('metodos_pagamento/delete/<int:pk>/', views.metodo_pagamento_delete, name='metodo_pagamento_delete'),
]
