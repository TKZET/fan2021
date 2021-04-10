from django.contrib import admin
from django.urls import path
from .views import VendaCreateView, ProdutoCreateView

urlpatterns = [
    path('cadastrar/venda', VendaCreateView.as_view(), name='cadastrar_venda'),
    path('cadastrar/produto', ProdutoCreateView.as_view(), name='cadastrar_produto')
]
