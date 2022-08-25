from django.urls import path
from .views import VistaNegocios, Usuarios

urlpatterns = [
    path('negocios/', VistaNegocios.as_view(), name='lista_negocios'),
    path('usuarios/', Usuarios.as_view(), name='usuarios'),
    path('negocios/<int:id>', VistaNegocios.as_view(), name='filtro_negocios')
    ]