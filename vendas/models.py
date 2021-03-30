from django.db import models


# Create your models here.
class Venda(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    data_venda = models.DateField(auto_now_add=True, blank=True, null=False)
    hora_venda = models.TimeField(auto_now_add=True, blank=True, null=False)
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    numero_venda = models.IntegerField(blank=False, null=False)
    observacao = models.TextField(blank=True, null=True)
    comprovante_venda = models.FileField(blank=True, null=True)
    exemplo_upload = models.FileField(upload_to='outro_diretorio/', null=True, blank=True)
    email_cliente = models.EmailField(blank=True, null=True)
    venda_concluida = models.BooleanField(blank=False, null=False)
    quantidade_itens = models.IntegerField(blank=True, null=False)
    produtos = models.ManyToManyField('Produto')
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1)


    def __str__(self):
        return str(self.pk)+ '-' + self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    tipo = models.CharField(max_length=255, blank=False, null=False)
    Valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.nome + '. R$: ' + str(self.Valor)


class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)

    def __str__(self):
        return self.nome
