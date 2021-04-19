from django.contrib import admin
from django.urls import path
from .views import VendaCreateView, ProdutoCreateView, VendaListView, VendaUpdateView

#Lembrar de por as virgulas.

urlpatterns = [
    path('cadastrar/venda', VendaCreateView.as_view(), name='cadastrar_venda'),
    path('cadastrar/produto', ProdutoCreateView.as_view(), name='cadastrar_produto'),
    path('listar/venda', VendaListView.as_view(), name='listar_venda'),
    path('atualizar/venda/<int:pk>', VendaUpdateView.as_view(), name='atualizar_venda'),
]