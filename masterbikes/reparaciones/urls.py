from django.urls import path
from . import views

app_name = 'reparaciones'

urlpatterns = [
    path('', views.lista_reparaciones, name='lista'),
    path('nueva/', views.nueva_reparacion, name='nueva'),
    path('<int:reparacion_id>/', views.detalle_reparacion, name='detalle'),
] 