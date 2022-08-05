from django.urls import path 
from .views import VistaNegocios

urlpatterns = [
    path('negocios/', VistaNegocios.as_view(), name='lista_negocios'),
    path('negocios/<int:id>', VistaNegocios.as_view(), name='filtro_negocios'),
               ]