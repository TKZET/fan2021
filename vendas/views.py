from django.shortcuts import render
from django.views.generic import CreateView
from .models import Venda, Produto
from django.urls import reverse_lazy

# Create your views here.


class VendaCreateView(CreateView):
    model = Venda
    template_name = 'cadastrar/venda.html'

    fields = '__all__'

    def get_sucess_url(self):
        return reverse_lazy('Cadastrar_venda')


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'cadastrar/produto.html'

    #Querendo todos os fields, colocar fields = __all__, caso contrário digitar o que tem abaixo.
    fields = ['nome', 'valor']

    def get_sucess_url(self):
        return reverse_lazy('Cadastrar_produto')