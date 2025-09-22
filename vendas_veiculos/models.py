from django.db import models


class Funcionario(models.Model):
    id = models.AutoField(primary_key=True, null=False, verbose_name="Identificador")
    nome = models.TextField(null=False, blank=False)
    cpf = models.TextField(null=False, blank=False)
    cargo = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"


class Veiculo(models.Model):
    id = models.AutoField(primary_key=True, null=False, verbose_name="Identificador")
    marca = models.TextField(null=False, blank=False)
    modelo = models.TextField(null=False, blank=False)
    ano = models.TextField(null=False, blank=False)
    preco = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = "Veiculo"
        verbose_name_plural = "Veiculos"


class Cliente(models.Model):
    id = models.AutoField(primary_key=True, null=False, verbose_name="Identificador")
    nome = models.TextField(null=False, blank=False)
    cpf = models.TextField(null=False, blank=False)
    telefone = models.TextField(null=False, blank=False)
    email = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


# Create your models here.


class Venda(models.Model):
    id = models.AutoField(primary_key=True, null=False, verbose_name="Identificador")
    data_venda = models.TextField(null=False, blank=False)
    valor_venda = models.TextField(null=False, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
