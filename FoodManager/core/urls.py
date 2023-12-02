from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastroProduto/", views.cadastroProduto, name="cadastroProduto"),
    path("listarProduto/", views.listarProdutos, name="listarProdutos"),
    path("listarRequerente/", views.listarRequerentes, name="listarRequerente"),
]
