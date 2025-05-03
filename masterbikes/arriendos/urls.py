from django.urls import path
from . import views

app_name = 'arriendos'

urlpatterns = [
    path('', views.lista_arriendos, name='lista'),
    path('nuevo/', views.nuevo_arriendo, name='nuevo'),
    path('<int:arriendo_id>/', views.detalle_arriendo, name='detalle'),
] 