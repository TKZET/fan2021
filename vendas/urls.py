from django.contrib import admin
from django.urls import path
from .views import VendaCreateView

urlpatterns = [
    path('cadastrar/venda', VendaCreateView.as_view(), name='cadastrar_venda'),
]
