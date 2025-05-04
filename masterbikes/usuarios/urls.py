from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='usuarios/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='usuarios/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='usuarios/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='usuarios/password_reset_complete.html'), name='password_reset_complete'),
] 