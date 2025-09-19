from rest_framework import viewsets

from vendas_veiculos import models, serializers


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = models.Funcionario.objects.all()
    serializer_class = serializers.FuncionarioSerializer
    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
    
class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = models.Veiculo.objects.all()
    serializer_class = serializers.VeiculoSerializer
    
class VendaViewSet(viewsets.ModelViewSet):
    queryset = models.Venda.objects.all()
    serializer_class = serializers.VendaSerializer            
# Create your views here.
