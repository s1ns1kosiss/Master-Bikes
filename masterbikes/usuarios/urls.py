from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    # Nuevas URLs para clientes
    path('cliente/perfil/', views.perfil_cliente, name='perfil_cliente'),
    path('cliente/arriendos/', views.ArriendosClienteListView.as_view(), name='arriendos_cliente'),
    path('cliente/reparaciones/', views.ReparacionesClienteListView.as_view(), name='reparaciones_cliente'),
] 