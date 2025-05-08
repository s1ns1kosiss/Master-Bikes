from django.urls import path
from . import views

app_name = 'promociones'

urlpatterns = [
    path('', views.lista_promociones, name='lista_promociones'),
    path('crear/', views.crear_promocion, name='crear_promocion'),
    path('<int:pk>/', views.detalle_promocion, name='detalle_promocion'),
    path('<int:pk>/editar/', views.editar_promocion, name='editar_promocion'),
    path('<int:pk>/desactivar/', views.desactivar_promocion, name='desactivar_promocion'),
] 