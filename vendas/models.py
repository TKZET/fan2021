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

    def _str_(self):
        return str(self.pk)+ '-' + self.nome


