from rest_framework import serializers

from vendas_veiculos import models

class FuncionarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Funcionario
        fields = "__all__"
        

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Cliente
        fields = "__all__"        
        

class VeiculoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Veiculo
        fields = "__all__"        
        

class VendaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Venda
        fields = "__all__"        