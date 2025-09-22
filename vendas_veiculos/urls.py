from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vendas_veiculos import views

router = DefaultRouter()
router.register(r'funcionarios', views.FuncionarioViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'veiculos', views.VeiculoViewSet)
router.register(r'vendas', views.VendaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]