from django.shortcuts import render
from django.views.generic import CreateView
from .models import Venda


# Create your views here.


class VendaCreateView(CreateView):
    model = Venda
    template_name = 'cadastrar/venda.html'

    fields = '__all__'