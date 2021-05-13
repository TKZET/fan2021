from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import Venda, Produto
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import VendaForm
# Create your views here.


class VendaCreateView(CreateView):
    form_class = VendaForm
    template_name = 'cadastrar/venda.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda cadastrada com suceso!')
        return reverse_lazy("listar_venda")


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'cadastrar/produto.html'

    #Querendo todos os fields, colocar fields = __all__, caso contrário digitar o que tem abaixo.
    fields = ['nome', 'valor']

    def get_success_url(self):
        messages.success(self.request, 'Produto cadastrado com sucesso!')
        return reverse_lazy('Cadastrar_produto')



class VendaListView(ListView):
    model = Venda
    template_name = 'listar/venda.html'
    paginate_by = 3


class VendaUpdateView(UpdateView):
    model = Venda
    template_name = 'atualizar/venda.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Venda atualizada com sucesso!')
        return reverse_lazy('listar_venda')